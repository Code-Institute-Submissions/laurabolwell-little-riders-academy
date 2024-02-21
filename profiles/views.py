from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def profile(request):
    """ Display the user's profile """
    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)
