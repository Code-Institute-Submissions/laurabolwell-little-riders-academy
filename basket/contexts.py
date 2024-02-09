def basket_contents(request):

    basket_items = []
    total = 0
    lesson_count = 0

    context = {
        'basket_items',
        'total',
        'lesson_count',
    }

    return context
