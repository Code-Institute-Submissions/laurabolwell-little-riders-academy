from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .forms import UserProfileForm


@login_required
def profile(request):
    """ Display the user's profile """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Billing information updated successfully.'
            )
        else:
            messages.error(
                request, 'Update failed. Please ensure the form is valid.'
            )

    form = UserProfileForm(instance=profile)
    bookings = profile.bookings.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'bookings': bookings,
        'on_profile_page': True,
    }

    return render(request, template, context)
