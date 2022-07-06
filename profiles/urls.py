from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('<user>', views.premium, name='premium'),
    path('<price>/<price2>', views.buy_premium, name='buy_premium'),
]
