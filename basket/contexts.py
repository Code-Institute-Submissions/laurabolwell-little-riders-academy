from django.shortcuts import get_object_or_404
from lessons.models import Lesson


def basket_contents(request):

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
                'date': date,
                'quantity': quantity,
                'lesson': lesson,
                })

    context = {
        'basket_items': basket_items,
        'total': total,
        'lesson_count': lesson_count,
    }

    return context
