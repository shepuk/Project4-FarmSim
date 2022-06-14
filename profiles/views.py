from django.shortcuts import render
from .models import Inventory


def profile(request):
    """ Display the user's profile. """

    items = Inventory.objects.all()

    context = {
        'items': items,
    }

    return render(request, 'profiles/profile.html', context)
