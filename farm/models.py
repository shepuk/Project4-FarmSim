from django.db import models
from django.contrib.auth.models import User
from store.models import Product
from profiles.models import Profile
from django.dispatch import receiver
from django.db.models.signals import post_save
from datetime import datetime 


class Farm(models.Model):
    """" The farm class, one unique to each user. Holds datatime info for harvesting time calculation """
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='farm')
    crop1 = models.ForeignKey(Product, null=True, blank=True, on_delete=models.SET_NULL, related_name='crop1')
    crop1_harvest_time = models.DateTimeField(null=True, blank=True)
    crop1_plant_time = models.DateTimeField(null=True, blank=True)
    crop2 = models.ForeignKey(Product, null=True, blank=True, on_delete=models.SET_NULL, related_name='crop2')
    crop2_harvest_time = models.DateTimeField(default=datetime.now, blank=True)
    crop2_plant_time = models.DateTimeField(null=True, blank=True)
    crop3 = models.ForeignKey(Product, null=True, blank=True, on_delete=models.SET_NULL, related_name='crop3')
    crop3_harvest_time = models.DateTimeField(default=datetime.now, blank=True)
    crop3_plant_time = models.DateTimeField(null=True, blank=True)
    crop4 = models.ForeignKey(Product, null=True, blank=True, on_delete=models.SET_NULL, related_name='crop4')
    crop4_harvest_time = models.DateTimeField(default=datetime.now, blank=True)
    crop4_plant_time = models.DateTimeField(null=True, blank=True)
    crop5 = models.ForeignKey(Product, null=True, blank=True, on_delete=models.SET_NULL, related_name='crop5')
    crop5_harvest_time = models.DateTimeField(default=datetime.now, blank=True)
    crop5_plant_time = models.DateTimeField(null=True, blank=True)
    crop6 = models.ForeignKey(Product, null=True, blank=True, on_delete=models.SET_NULL, related_name='crop6')
    crop6_harvest_time = models.DateTimeField(default=datetime.now, blank=True)
    crop6_plant_time = models.DateTimeField(null=True, blank=True)
    crop7 = models.ForeignKey(Product, null=True, blank=True, on_delete=models.SET_NULL, related_name='crop7')
    crop7_harvest_time = models.DateTimeField(default=datetime.now, blank=True)
    crop7_plant_time = models.DateTimeField(null=True, blank=True)
    crop8 = models.ForeignKey(Product, null=True, blank=True, on_delete=models.SET_NULL, related_name='crop8')
    crop8_harvest_time = models.DateTimeField(default=datetime.now, blank=True)
    crop8_plant_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_farm(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        Farm.objects.create(user=instance)
