from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    """ Profile data primarily used to check currency and premium membership """
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(max_length=500, default="My Bio")
    is_premium = models.TextField(default="no")
    coins = models.DecimalField(default=50, max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        Profile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.profile.save()
