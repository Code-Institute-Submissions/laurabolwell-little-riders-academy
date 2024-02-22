from django.shortcuts import render
from .models import Question


def view_faqs(request):
    """ A view to display all FAQs """
    questions = Question.objects.all()

    context = {
        'questions': questions,
    }
    
    return render(request, 'faqs/faqs.html', context)
