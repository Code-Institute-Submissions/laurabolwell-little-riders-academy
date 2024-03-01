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

    # Check if there is already a lesson of that type in the basket
    if lesson_id in list(basket.keys()):
        # If so, check if there is already a lesson on that date
        if date in basket[lesson_id].keys():
            # If so, increase the quantity
            basket[lesson_id][date] += quantity
            messages.success(
                request,
                f'Updated {lesson.name} on {date} quantity '
                f'to {basket[lesson_id][date]}'
            )
        # If not, add the new date and quantity to the object
        else:
            basket[lesson_id][date] = quantity
            messages.success(
                request, f'Added {lesson.name} on {date} to your basket'
            )
    # If no lesson of that type, add it to the basket
    else:
        basket[lesson_id] = {}
        # Then add the date and quantity
        basket[lesson_id][date] = quantity
        messages.success(
            request, f'Added {lesson.name} on {date} to your basket'
        )

    request.session['basket'] = basket
    return redirect(redirect_url)


def adjust_basket(request, lesson_id):
    """ Adjust the quantity of a lesson on a given date """
    lesson = Lesson.objects.get(pk=lesson_id)
    quantity = int(request.POST.get('quantity'))
    date = request.POST.get('lesson_date')
    basket = request.session.get('basket', {})

    if quantity > 0:
        basket[lesson_id][date] = quantity
        messages.success(
            request,
            f'Updated {lesson.name} on {date} quantity to '
            f'{basket[lesson_id][date]}'
        )
    else:
        del basket[lesson_id][date]
        if not basket[lesson_id]:
            del basket[lesson_id]
        messages.success(
            request, f'Removed {lesson.name} on {date} from your basket'
        )

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))


def remove_from_basket(request, lesson_id):
    """ Remove the lesson from the basket """
    lesson = Lesson.objects.get(pk=lesson_id)
    try:
        date = request.POST.get('lesson_date')
        basket = request.session.get('basket', {})

        del basket[lesson_id][date]
        messages.success(
            request, f'Removed {lesson.name} on {date} from your basket'
        )

        request.session['basket'] = basket
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
