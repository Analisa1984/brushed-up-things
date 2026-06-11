from django.db import models
from django.db.models import Sum
from django.conf import settings
from artwork.models import Artwork
from django_countries.fields import CountryField


# Create your models here.
class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    town_or_city = models.CharField(max_length=50, null=False, blank=False)
    county = models.CharField(max_length=60, null=True, blank=True)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    post_code = models.CharField(max_length=30, null=True, blank=True)
    shipping_cost = models.DecimalField(max_digits=6,
                                        decimal_places=2,
                                        null=False,
                                        default=0)
    order_total = models.DecimalField(max_digits=6,
                                      decimal_places=2,
                                      null=False,
                                      default=0)
    grand_total = models.DecimalField(max_digits=6,
                                      decimal_places=2,
                                      null=False,
                                      default=0)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order,
                              null=False,
                              blank=False,
                              on_delete=models.CASCADE,
                              related_name='lineitems')
    artwork = models.ForeignKey(Artwork,
                                null=False,
                                blank=False,
                                on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6,
                                         decimal_places=2,
                                         null=False,
                                         default=0)
