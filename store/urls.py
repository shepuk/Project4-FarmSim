from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('<product_id>', views.product_detail, name='product_detail'),
    path('add/<product_id>/', views.add_to_user_inventory, name='add_to_user_inventory'),
]
