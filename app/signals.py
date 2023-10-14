from django.db.models.signals import post_save, pre_delete
from .models import image
from django.contrib.auth.models import User
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        image.objects.create(user=instance)