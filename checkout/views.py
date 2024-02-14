from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings

from .forms import BookingForm
from .models import Booking, BookingItem
from lessons.models import Lesson
from basket.contexts import basket_contents

import stripe


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == "POST":
        basket = request.session.get('basket', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }
        booking_form = BookingForm(form_data)
        if booking_form.is_valid():
            booking = booking_form.save()
            for lesson_id, lesson_data in basket.items():
                try:
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
                except Lesson.DoesNotExist:
                    messages.error(request, (
                        "One of the lessons in your basket wasn't \
                            found in our database. "
                        "Please call us for assistance!")
                    )
                    booking.delete()
                    return redirect(reverse('view_basket'))

            request.session['save_info'] = 'save_info' in request.POST
            return redirect(reverse(
                'checkout_success', args=[booking.booking_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information ')

    else:
        basket = request.session.get('basket', {})
        if not basket:
            messages.error(
                request, "There's nothing in yout basket at the moment")
            return redirect(reverse('lessons'))

        current_basket = basket_contents(request)
        total = current_basket['total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY
        )

        booking_form = BookingForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'booking_form': booking_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, booking_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    booking = get_object_or_404(Booking, booking_number=booking_number)
    messages.success(request, f'Booking successful! \
        Your booking number is {booking_number}. A \
        confirmation email will be sent to {booking.email}.')

    if 'basket' in request.session:
        del request.session['basket']

    template = 'checkout/checkout_success.html'
    context = {
        'booking': booking,
    }

    return render(request, template, context)
