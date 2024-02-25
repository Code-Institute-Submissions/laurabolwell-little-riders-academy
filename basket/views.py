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


def adjust_basket(request, lesson_id):
    """ Adjust the quantity of the lesson on a given date """
    print("correct view")
    lesson = Lesson.objects.get(pk=lesson_id)
    print("lesson")
    date = request.POST.get('lesson_date')
    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})
    print("lesson:", lesson)
    print("date:", date)
    print("quantity", quantity)
    print("basket", basket)

    if quantity > 0:
        basket[lesson_id][date] = quantity
        messages.success(request, f'Updated {lesson.name} on {date} quantity to {basket[lesson_id][date]}')
    else:
        del basket[lesson_id][date]
        messages.success(request, f'Removed {lesson.name} on {date} from your basket')

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))


def remove_from_basket(request, lesson_id):
    """ Remove the lesson from the basket """
    try:
        date = request.POST.get('lesson_date')
        basket = request.session.get('basket', {})

        del basket[lesson_id][date]

        request.session['basket'] = basket
        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=500)
