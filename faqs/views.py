from django.shortcuts import render, redirect, reverse, get_object_or_404
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


def edit_question(request, question_id):
    """ Edit a question in the FAQs list """
    question = get_object_or_404(Question, pk=question_id)

    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated question')
            return redirect(reverse('faqs'))
        else:
            messages.error(
                request,
                'Cannot add question. Please ensure the form is valid.'
            )

    else:
        form = QuestionForm(instance=question)

    template = 'faqs/edit_question.html'
    context = {
        'form': form,
        'question': question
    }

    return render(request, template, context)
