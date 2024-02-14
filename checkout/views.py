from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import BookingForm


def checkout(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "There's nothing in yout basket at the moment")
        return redirect(reverse('lessons'))

    booking_form = BookingForm()
    template = 'checkout/checkout.html'
    context = {
        'booking_form': booking_form,
        'stripe_public_key': 'pk_test_51ObSJNDbhOsfDiIzHeY3zTeS7vM3BH7fcTT8FkRZw2Zvro3OhuefF6xoH6XPqQ6dacfyTTDuqEck7IXGQRT0lsig00mY6GLxV8',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
