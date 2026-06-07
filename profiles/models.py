from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
        )
    default_address = models.CharField(max_length=250, blank=True, null=True)
    default_contact_number = models.CharField(
        max_length=20,
        blank=True,
        null=True
        )

    def __str__(self):
        return f"{self.user.username}'s Profile"


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()
