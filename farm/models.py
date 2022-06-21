from django.db import models
from django.contrib.auth.models import User
from store.models import Product
from profiles.models import Profile
from django.dispatch import receiver
from django.db.models.signals import post_save
from datetime import datetime 

# Create your models here.
class Farm(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='farm')
    crop1 = models.TextField(null=True, blank=True)
    crop1_harvest_time = models.DateTimeField(null=True, blank=True)
    crop2 = models.TextField(null=True, blank=True)
    crop2_harvest_time = models.DateTimeField(default=datetime.now, blank=True)
    crop3 = models.TextField(null=True, blank=True)
    crop3_harvest_time = models.DateTimeField(default=datetime.now, blank=True)
    crop4 = models.TextField(null=True, blank=True)
    crop4_harvest_time = models.DateTimeField(default=datetime.now, blank=True)
    crop5 = models.TextField(null=True, blank=True)
    crop5_harvest_time = models.DateTimeField(default=datetime.now, blank=True)
    crop6 = models.TextField(null=True, blank=True)
    crop6_harvest_time = models.DateTimeField(default=datetime.now, blank=True)
    crop7 = models.TextField(null=True, blank=True)
    crop7_harvest_time = models.DateTimeField(default=datetime.now, blank=True)
    crop8 = models.TextField(null=True, blank=True)
    crop8_harvest_time = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_farm(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        Farm.objects.create(user=instance)
    # Existing users: just save the profile
