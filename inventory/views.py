from django.shortcuts import render
from .models import Inventory
from .models import Product


def inventory(request):
    """ Display the user's profile. """

    items = Inventory.objects.all()
    product = Product.objects.all()

    context = {
        'items': items,
        'product': product,
    }

    return render(request, 'inventory/inventory.html', context)
