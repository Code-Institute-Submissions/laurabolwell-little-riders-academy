def basket_contents(request):

    basket_items = []
    total = 0
    lesson_count = 0

    context = {
        'basket_items': basket_items,
        'total': total,
        'lesson_count': lesson_count,
    }

    return context
