from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages

from lessons.models import Lesson


def view_basket(request):
    """ A view to show the basket contents """

    return render(request, 'basket/basket.html')


def add_to_basket(request, lesson_id):
    """ A view to add a lesson, including quantity and date, to the basket """
    lesson = Lesson.objects.get(pk=lesson_id)
    date = request.POST.get('date')
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if lesson_id in list(basket.keys()):
        if date in basket[lesson_id].keys():
            basket[lesson_id][date] += quantity
            messages.success(request, f'Updated {lesson.name} on {date} quantity to {basket[lesson_id][date]}')
        else:
            basket[lesson_id][date] = quantity
            messages.success(request, f'Added {lesson.name} on {date} to your basket')
    else:
        basket[lesson_id] = {}
        basket[lesson_id][date] = quantity
        messages.success(request, f'Added {lesson.name} on {date} to your basket')

    request.session['basket'] = basket
    return redirect(redirect_url)
