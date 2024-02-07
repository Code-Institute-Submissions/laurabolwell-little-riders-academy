from django.shortcuts import render
from .models import Lesson


def all_lessons(request):
    """ A view to show all lessons """

    lessons = Lesson.objects.all()

    context = {
        'lessons': lessons,
    }

    return render(request, 'lessons/lessons.html', context)