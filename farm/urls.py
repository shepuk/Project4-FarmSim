from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.farm, name='farm'),
    path('<item>', views.plant_crop, name='plant_crop'),
]
