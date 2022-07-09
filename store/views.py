from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from inventory.models import Inventory
from profiles.models import Profile
from django.contrib import messages
from django.contrib.auth.models import User


def store(request):
    """ lists all products """
    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'store/store.html', context)


def product_detail(request, product_name):
    """ directs to a page which displays detailed item info """
    product = get_object_or_404(Product, name=product_name)

    context = {
        'product': product,
    }

    return render(request, 'store/product_detail.html', context)


def add_to_user_inventory(request, product_id):
    """ Adds or updates entry to inventory model with current user as owner """
    """ Updates current coins held by user and checks user has enough coins """
    owner = request.user
    item = get_object_or_404(Product, pk=product_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    currentuser = Profile.objects.get(user=owner)

    if Inventory.objects.filter(owner=owner, item=item).exists():
        existingentry = Inventory.objects.get(owner=owner, item=item)
        existingentry.quantity += quantity
        if item.price * quantity <= currentuser.coins:
            currentuser.coins = currentuser.coins - item.price * quantity
            currentuser.save()
            existingentry.save()
            messages.success(request, f"{quantity} {item} added to inventory")
        else:
            messages.success(request, f"Not enough coins, {item.price * quantity} required.")
    else:
        if item.price * quantity <= currentuser.coins:
            currentuser.coins = currentuser.coins - item.price * quantity
            currentuser.save()
            newentry = Inventory(owner=owner, item=item, quantity=quantity)
            newentry.save()
            messages.success(request, f"{quantity} {item} added to inventory")
        else:
            messages.success(request, f"Not enough coins, {item.price * quantity} required.")
    return redirect(redirect_url)
