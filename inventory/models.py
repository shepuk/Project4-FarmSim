from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from store.models import Product

class Inventory(models.Model):
    owner = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    item = models.ForeignKey(Product, null=True, blank=True, on_delete=models.SET_NULL)
    quantity = models.DecimalField(default=5.00, max_digits=5, decimal_places=2)


    def __str__(self):
        return self.owner.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        Inventory.objects.create(user=instance)
    # Existing users: just save the profile

