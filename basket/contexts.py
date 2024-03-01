from django.shortcuts import get_object_or_404
from lessons.models import Lesson
from datetime import datetime


def basket_contents(request):
    """
    Returns all the lessons currently in the basket,
    the number of items and the total
    """
    basket_items = []
    total = 0
    lesson_count = 0
    basket = request.session.get('basket', {})

    for lesson_id, lesson_data in basket.items():
        lesson = get_object_or_404(Lesson, pk=lesson_id)
        for date in lesson_data:
            quantity = lesson_data[date]
            total += quantity * lesson.price
            lesson_count += quantity
            basket_items.append({
                'lesson_id': lesson_id,
                'date': datetime.strptime(date, "%Y-%m-%d").date(),
                'quantity': quantity,
                'lesson': lesson,
                })

    context = {
        'basket_items': basket_items,
        'total': total,
        'lesson_count': lesson_count,
    }

    return context
