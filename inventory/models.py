from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from store.models import Product

class Inventory(models.Model):
    """ unique item field, with related field to user and product """
    owner = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    item = models.ForeignKey(Product, null=True, blank=True, on_delete=models.SET_NULL, related_name='product')
    quantity = models.DecimalField(default=5.00, max_digits=5, decimal_places=0)


    def __str__(self):
        return self.owner.username

