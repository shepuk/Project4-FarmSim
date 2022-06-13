from django.shortcuts import render

# Create your views here.

def farm (request):
    return render(request, 'farm/farm.html')