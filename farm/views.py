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


def plant_crop(request, item, cropslot):

    items = Inventory.objects.all()

    # item = get_object_or_404(Product, name=item_item)
    owner = request.user # get user
    redirect_url = request.POST.get('redirect_url')
    crop = Inventory.objects.get(owner=owner, item__name=item) # get item from user inventory
    product = get_object_or_404(Product, name=item) # get product for growtime ref.

    if crop.quantity >= 1:
        crop.quantity = crop.quantity - 1
        crop.save()
    if crop.quantity <= 0:
        crop.delete()

    # quickfix for UK time - need to add timezomeaware date generation (pytz)
    harvest_time = datetime.now() + timedelta(hours=1, seconds=180)

    if Farm.objects.filter(user=owner).exists():
        farm = Farm.objects.get(user=owner)
        setattr(farm, cropslot, item)
        setattr(farm, "{}_harvest_time".format(cropslot), harvest_time)

        farm.save()
    else:
        cropplant = Farm(user=owner, cropslot=item, cropslot_harvest_time=harvest_time)
        cropplant.save()

    items = Inventory.objects.all()

    context = {
        'items': items,
    }
    
    return redirect(redirect_url)