from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile", blank=True, null=True)
    photo = models.ImageField(upload_to='media/', blank=True, null=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile(user=instance).save()



class ImageNFT(models.Model):
    imagenft = models.ImageField(upload_to='media/', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="profile_user", null=True)

