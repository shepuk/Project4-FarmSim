from django.shortcuts import render

# Create your views here.

""" docstring for all below - simple HTML renders for each page """

def index (request):
    return render (request, 'home/index.html')

def help (request):
    return render (request, 'home/help.html')

def about (request):
    return render (request, 'home/about.html')