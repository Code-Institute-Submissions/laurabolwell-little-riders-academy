from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages


from .models import Lesson
from .forms import LessonForm


def all_lessons(request):
    """ A view to show all lessons """

    lessons = Lesson.objects.all()

    context = {
        'lessons': lessons,
    }

    return render(request, 'lessons/lessons.html', context)


def lesson_details(request, lesson_id):
    """ A view to show individual lesson details """

    lesson = get_object_or_404(Lesson, pk=lesson_id)

    context = {
        'lesson': lesson,
    }

    return render(request, 'lessons/lesson_details.html', context)


def add_lesson(request):
    """ Add a lesson to the site """
    if request.method == 'POST':
        form = LessonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added lesson!')
            return redirect(reverse('lessons'))
        else:
            messages.error(request, 'Failed to add lesson. Please ensure the form is valid.')
    else:
        form = LessonForm()

    template = 'lessons/add_lesson.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
