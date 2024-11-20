# from django.contrib.auth.models import User
# from .models import Profile
# from django.db.models.signals import post_save
# from django.dispatch import receiver







# @receiver(post_save, sender=User)
# def create_profile(sender,  instance,   created,  *args,  **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
from django.contrib.auth.models import User
from .models import Profile
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    Create a Profile for the user when a new User is created.
    """
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    """
    Save the Profile when the User is saved.
    """
    instance.profile.save()
