from django.shortcuts import render, redirect, reverse
from django.contrib import messages


from profiles.models import UserProfile
from .models import Contact
from .forms import ContactForm


def contact(request):
    """ A view to return the contact page """
    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(
                request,
                'Message sent. We will aim to get back to you within 48 hours.'
            )
            return redirect(reverse('lessons'))
        else:
            messages.error(
                request,
                'Cannot add question. Please ensure the form is valid.'
            )
    if request.user.is_authenticated:
        # If user is logged in, fill form with profile details
        try:
            profile = UserProfile.objects.get(user=request.user)
            contact_form = ContactForm(initial={
                    'name': profile.user.get_full_name(),
                    'email': profile.user.email,
                })
        except UserProfile.DoesNotExist:
            contact_form = ContactForm()
    else:
        contact_form = ContactForm()
    template = 'contact/contact.html'
    context = {
        'contact_form': contact_form
    }
    return render(request, template, context)


def view_queries(request):
    """ A view to display all queries """
    queries = Contact.objects.all()

    context = {
        'queries': queries,
    }

    template = 'contact/view_queries.html'

    return render(request, template, context)
