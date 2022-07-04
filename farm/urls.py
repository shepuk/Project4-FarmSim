from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.farm, name='farm'),
    path('<item>/<cropslot>/<number>', views.plant_crop, name='plant_crop'),
    path('<crop>/<position>', views.harvest_crop, name='harvest_crop'),
]
