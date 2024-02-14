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
    }

    return render(request, template, context)
