from django.shortcuts import render, get_object_or_404
from .models import Lesson


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
