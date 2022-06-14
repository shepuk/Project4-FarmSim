from django.db import models
from django.contrib.auth.models import User
from store.models import Product
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, default="My Bio")
    is_premium = models.TextField(default="no")
    coins = models.DecimalField(default=50.00, max_digits=5, decimal_places=2)
    crop1 = models.TextField(null=True)
    crop2 = models.TextField(null=True)
    crop3 = models.TextField(null=True)
    crop4 = models.TextField(null=True)
    crop5 = models.TextField(null=True)
    crop6 = models.TextField(null=True)
    crop7 = models.TextField(null=True)
    crop8 = models.TextField(null=True)

    def __str__(self):
        return self.name.username


class Inventory(models.Model):
    owner = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    item = models.OneToOneField(Product, null=True, on_delete=models.CASCADE)
    quantity = models.DecimalField(default=5.00, max_digits=5, decimal_places=2)


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if instance.profile:
        instance.profile.save()
        return
    else:
        Profile.objects.create(user=instance)
        instance.profile.save()

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
