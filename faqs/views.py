from django.shortcuts import render, redirect, reverse
from django.contrib import messages

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
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added question')
            return redirect(reverse('faqs'))
        else:
            messages.error(
                request,
                'Cannot add question. Please ensure the form is valid.'
            )
    else:
        form = QuestionForm()

    template = 'faqs/add_question.html'
    context = {
        'form': form
    }

    return render(request, template, context)
