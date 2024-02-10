from django.shortcuts import render, redirect


def view_basket(request):
    """ A view to show the basket contents """

    return render(request, 'basket/basket.html')


def add_to_basket(request, lesson_id):
    date = request.POST.get('date')
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if lesson_id in list(basket.keys()):
        if date in basket[lesson_id].keys():
            basket[lesson_id][date] += quantity
        else:
            basket[lesson_id][date] = quantity
    else:
        basket[lesson_id] = {}
        basket[lesson_id][date] = quantity

    request.session['basket'] = basket
    print(request.session['basket'])
    return redirect(redirect_url)
