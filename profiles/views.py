from django.shortcuts import render, redirect
from .models import Profile
import stripe
from django.conf import settings
import datetime
import os


def profile(request):
    print('profile')
    """ Display the user's profile. """

    context = {}

    return render(request, 'profiles/profile.html', context)


def premium(request, user):
    """ Display the premium purchase page. """

    context = {}

    return render(request, 'profiles/premium.html', context)


def buy_premium(request, price, price2):
    """ Creates and redirects to a Stripe payment service """
    user=request.user

    STRIPE_KEY = os.environ.get('STRIPE_KEY')

    stripe.api_key = STRIPE_KEY

    session = stripe.checkout.Session.create(
        success_url="https://sunrise-farm.herokuapp.com/profile/"+{user}+"/success",
        cancel_url="https://sunrise-farm.herokuapp.com/profile",
        line_items=[
            {
                "price": 'price_1LIeqUAzWoPkZ58IkIq0o5Xe',
                "quantity": 1,
            },
        ],
        mode="payment",
        )
    
    return redirect(session.url)


def premium_success(request):
    """ Adds premium membership to user account """
    user = request.user
    profile = Profile.objects.get(user=user)
    profile.is_premium = 'yes'
    profile.save()
    return render(request, 'profiles/purchased.html')