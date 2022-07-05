from django.urls import path
from . import views

urlpatterns = [
    path('', views.market, name='market'),
    path('<item>/<sellprice>/', views.sell_item, name='sell_item'),
]
