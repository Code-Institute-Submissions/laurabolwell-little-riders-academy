from django.shortcuts import render

from testimonials.models import Testimonial


def index(request):
    """ A view to return the index page """
    testimonials = Testimonial.objects.all()

    context = {
        'testimonials': testimonials,
    }
    template = 'home/index.html'

    return render(request, template, context)
