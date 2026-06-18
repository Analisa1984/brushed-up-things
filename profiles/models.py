from django.db import models
from django.conf import settings
from django_countries.fields import CountryField


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    default_phone_number = models.CharField(
        max_length=20, blank=True, null=True)
    default_street_address1 = models.CharField(
        max_length=80, blank=True, null=True)
    default_street_address2 = models.CharField(
        max_length=80, blank=True, null=True)
    default_town_or_city = models.CharField(
        max_length=40, blank=True, null=True)
    default_county = models.CharField(max_length=80, blank=True, null=True)
    default_postcode = models.CharField(max_length=20, blank=True, null=True)
    default_country = CountryField(
        blank_label='Country', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
