from django.shortcuts import render
from .models import Product
# Create your views here.


def store(request):

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'store/store.html', context)
