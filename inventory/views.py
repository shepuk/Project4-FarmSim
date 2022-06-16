from django.shortcuts import render
from .models import Inventory


def inventory(request):
    """ Display the user's profile. """

    items = Inventory.objects.all()

    context = {
        'items': items,
    }

    return render(request, 'inventory/inventory.html', context)
