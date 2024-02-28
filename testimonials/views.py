from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from profiles.models import UserProfile
from .forms import TestimonialForm


def leave_testimonial(request):
    """ A view to return the testimonial form """
    if request.method == "POST":
        form = TestimonialForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated:
                user = request.user
                new_testimonial = form.save(commit=False)
                new_testimonial.user = user
                new_testimonial.save()
            else:
                form.save()
            messages.success(
                request,
                'Testimonial saved, thank you!'
            )
            return redirect(reverse('lessons'))
        else:
            messages.error(
                request,
                'Cannot save testimonial. Please ensure the form is valid.'
            )

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        bookings = profile.bookings.all()
        if bookings:
            testimonial_form = TestimonialForm()
            template = 'testimonials/leave_testimonial.html'
            context = {
                'testimonial_form': testimonial_form
            }
            return render(request, template, context)
        else:
            messages.error(
                request,
                'You must make a booking before you can leave a testimonial.'
            )
            return redirect(reverse('lessons'))
    else:
        messages.error(request, 'You must log in to leave a testimonial.')
    return redirect(reverse('account_login'))
