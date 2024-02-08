from django.shortcuts import render


def view_basket(request):
    """ A view to show the basket contents """

    return render(request, 'basket/basket.html')