from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from profiles.models import Profile
from inventory.models import Inventory
from store.models import Product
from .models import Farm
from datetime import datetime, timedelta


def farm (request):

    items = Inventory.objects.all()

    context = {
        'items': items,
    }

    return render(request, 'farm/farm.html', context)


def plant_crop(request, item):

    items = Inventory.objects.all()

    # item = get_object_or_404(Product, name=item_item)
    owner = request.user # get user
    redirect_url = request.POST.get('redirect_url')
    crop = Inventory.objects.get(owner=owner, item__name=item) # get item from user inventory
    print(crop.item)
    product = get_object_or_404(Product, name=item) # get product for growtime ref.

    crop.quantity = crop.quantity - 1
    if crop.quantity < 1:
        crop.delete()

    plant_time = datetime.now() + timedelta(seconds=120)

    cropplant = Farm(user=owner, crop1=item, crop1_harvest_time=plant_time)
    crop.save()


    items = Inventory.objects.all()
    context = {
        'items': items,
    }
    
    return redirect(redirect_url)