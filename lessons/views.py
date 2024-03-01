from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required


from .models import Lesson
from .forms import LessonForm


def all_lessons(request):
    """ A view to show all lessons """
    lessons = Lesson.objects.order_by("min_age", "max_age")
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


@login_required
def add_lesson(request):
    """ Add a lesson to the site """
    # Only allow superusers to add a lesson
    if not request.user.is_superuser:
        messages.error(
            request, 'You do not have permission to access this page.'
        )
        return redirect(reverse('lessons'))

    if request.method == 'POST':
        form = LessonForm(request.POST, request.FILES)
        if form.is_valid():
            lesson = form.save()
            messages.success(request, 'Successfully added lesson!')
            return redirect(reverse('lesson_details', args=[lesson.id]))
        else:
            messages.error(
                request,
                'Failed to add lesson. Please ensure the form is valid.'
            )
    else:
        form = LessonForm()

    template = 'lessons/add_lesson.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_lesson(request, lesson_id):
    """ Edit a lesson's details """
    # Only allow superusers to edit a lesson
    if not request.user.is_superuser:
        messages.error(
            request, 'You do not have permission to access this page.'
        )
        return redirect(reverse('lessons'))

    lesson = get_object_or_404(Lesson, pk=lesson_id)
    if request.method == 'POST':
        form = LessonForm(request.POST, request.FILES, instance=lesson)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated lesson!')
            return redirect(reverse('lesson_details', args=[lesson.id]))
        else:
            messages.error(
                request,
                'Failed to update lesson. Please ensure the form is valid.'
            )
    else:
        form = LessonForm(instance=lesson)
        messages.info(request, f'You are editing {lesson.name}')

    template = 'lessons/edit_lesson.html'
    context = {
        'form': form,
        'lesson': lesson
    }

    return render(request, template, context)


@login_required
def delete_lesson(request, lesson_id):
    """ Delete a lesson from the site """
    # Only allow superusers to delete a lesson
    if not request.user.is_superuser:
        messages.error(
            request, 'You do not have permission to access this page.'
        )
        return redirect(reverse('lessons'))

    lesson = get_object_or_404(Lesson, pk=lesson_id)
    lesson.delete()
    messages.success(request, 'Lesson deleted!')
    return redirect(reverse('lessons'))
