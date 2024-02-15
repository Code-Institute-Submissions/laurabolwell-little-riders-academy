from django.http import HttpResponse

from .models import Booking, BookingItem
from lessons.models import Lesson

import json
import time
import stripe


class StripeWH_Handler:
    """ Handle Stripe Webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook or event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200
        )

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        pid = intent.id
        basket = intent.metadata.basket
        save_info = intent.metadata.save_info

        # Get the Charge object
        stripe_charge = stripe.Charge.retrieve(
            intent.latest_charge
        )

        billing_details = stripe_charge.billing_details
        booking_total = round(stripe_charge.amount / 100, 2)

        # Clean data in the billing details
        for field, value in billing_details.address.items():
            if value == "":
                billing_details.address[field] = None

        booking_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                booking = Booking.objects.get(
                    full_name__iexact=billing_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=billing_details.phone,
                    country__iexact=billing_details.address.country,
                    # postcode__iexact=billing_details.address.postal_code,
                    town_or_city__iexact=billing_details.address.city,
                    street_address1__iexact=billing_details.address.line1,
                    street_address2__iexact=billing_details.address.line2,
                    county__iexact=billing_details.address.state,
                    booking_total=booking_total,
                    original_basket=basket,
                    stripe_pid=pid,
                )
                booking_exists = True
                break
            except Booking.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if booking_exists:
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified booking already in database',
                status=200)
        else:
            booking = None
            try:
                booking = Booking.objects.create(
                    full_name=billing_details.name,
                    email=billing_details.email,
                    phone_number=billing_details.phone,
                    country=billing_details.address.country,
                    postcode=billing_details.address.postal_code,
                    town_or_city=billing_details.address.city,
                    street_address1=billing_details.address.line1,
                    street_address2=billing_details.address.line2,
                    county=billing_details.address.state,
                    original_basket=basket,
                    stripe_pid=pid,
                )
                for lesson_id, lesson_data in json.loads(basket).items():
                    lesson = Lesson.objects.get(id=lesson_id)
                    for date in lesson_data:
                        quantity = lesson_data[date]
                        booking_item = BookingItem(
                            booking=booking,
                            lesson=lesson,
                            date=date,
                            quantity=quantity
                        )
                        booking_item.save()
            except Exception as e:
                if booking:
                    booking.delete()
                return HttpResponse(content=f'Webhook received: {event["type"]} | ERROR: {e}')
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created booking in webhook',
            status=200
        )

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )
