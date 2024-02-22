from django.shortcuts import render
from .models import Question
from .forms import QuestionForm


def view_faqs(request):
    """ A view to display all FAQs """
    questions = Question.objects.all()

    context = {
        'questions': questions,
    }

    return render(request, 'faqs/faqs.html', context)


def add_question(request):
    """ Add a question to the FAQs """
    form = QuestionForm()
    template = 'faqs/add_question.html'
    context = {
        'form': form
    }

    return render(request, template, context)
