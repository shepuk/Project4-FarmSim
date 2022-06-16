from django.db import models
from django.contrib.auth.models import User
from store.models import Product
from django.db.models.signals import post_save
from django.dispatch import receiver


class Inventory(models.Model):
    owner = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    item = models.ForeignKey(Product, null=True, blank=True, on_delete=models.SET_NULL)
    quantity = models.DecimalField(default=5.00, max_digits=5, decimal_places=2)


@receiver(post_save, sender=User)
def create_or_update_user_inventory(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if instance.inventory:
        instance.inventory.save()
        return
    else:
        Inventory.objects.create(user=instance)
        instance.inventory.save()
