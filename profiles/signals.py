from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Automatically create or update a UserProfile whenever
    a User object is created.
    """

    if created:
        UserProfile.objects.get_or_create(user=instance)
    instance.userprofile.save()
