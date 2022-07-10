from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('help/', views.help, name='help'),
    path('about/', views.about, name='about'),
]
