from django.shortcuts import render, get_object_or_404, redirect
from store.models import Product
from inventory.models import Inventory
from profiles.models import Profile
from django.contrib import messages
from django.contrib.auth.models import User

def market(request):
    """ displays market page """
    inventory = Inventory.objects.all()
    user=request.user

    context = {
        'inventory': inventory,
        'user': user
    }

    return render(request, 'market/market.html', context)


def sell_item(request, item, sellprice):
    """ removed from owner inventory, logic to check coin amount and if user has enough to sell """
    owner = request.user
    user = Profile.objects.get(user=owner)
    crop = Inventory.objects.get(owner=owner, item__name=item)
    quantity = int(request.POST.get('quantity'))

    if crop.quantity >= int(quantity):
        crop.quantity = crop.quantity - int(quantity)
        user.coins = user.coins + (int(sellprice) * int(quantity))
        user.save()
        crop.save()
        messages.success(request, f"{ quantity } { item } sold for {(int(sellprice) * int(quantity))} coins.")
    elif crop.quantity < int(quantity):
        messages.success(request, f"You only own { crop.quantity } { item } and are trying to sell { quantity }!")

    if crop.quantity <= 0:
        crop.delete()

    return redirect(market)
