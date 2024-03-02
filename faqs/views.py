from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Question
from .forms import QuestionForm


def view_faqs(request):
    """ A view to display all FAQs """
    questions = Question.objects.all()

    context = {
        'questions': questions,
    }

    template = 'faqs/faqs.html'
    return render(request, template, context)


@login_required
def add_question(request):
    """ Add a question to the FAQs """
    # Can only be viewed by superusers
    if not request.user.is_superuser:
        messages.error(
            request, 'You do not have permission to access this page.'
        )
        return redirect(reverse('faqs'))

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


@login_required
def edit_question(request, question_id):
    """ Edit a question in the FAQs list """
    if not request.user.is_superuser:
        messages.error(
            request, 'You do not have permission to access this page.'
        )
        return redirect(reverse('faqs'))

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


@login_required
def delete_question(request, question_id):
    """ Delete a question from the FAQs list """
    if not request.user.is_superuser:
        messages.error(
            request, 'You do not have permission to access this page.'
        )
        return redirect(reverse('faqs'))
    question = get_object_or_404(Question, pk=question_id)
    question.delete()
    messages.success(request, 'Question deleted!')
    return redirect(reverse('faqs'))
