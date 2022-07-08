from django.shortcuts import render, redirect
import stripe
from django.conf import settings
import datetime


def profile(request):
    print('profile')
    """ Display the user's profile. """

    context = {}

    return render(request, 'profiles/profile.html', context)


def premium(request, user):
    """ Display the user's profile. """

    context = {}

    return render(request, 'profiles/premium.html', context)

def buy_premium(request, price, price2):

    STRIPE_KEY = settings.STRIPE_KEY

    print(STRIPE_KEY)

    stripe.api_key = STRIPE_KEY

    session = stripe.checkout.Session.create(
        success_url="https://8000-shepuk-project4farmsim-xhmhcyec1z2.ws-eu51.gitpod.io/profile/1",
        cancel_url="https://8000-shepuk-project4farmsim-xhmhcyec1z2.ws-eu51.gitpod.io/profile/1",
        line_items=[
            {
                "price": 'price_1LIeqUAzWoPkZ58IkIq0o5Xe',
                "quantity": 1,
            },
        ],
        mode="payment",
        )
    print(session.url)

    context = {}
    
    return redirect(session.url)
