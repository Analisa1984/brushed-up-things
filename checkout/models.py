import uuid
from django.db import models
from django.db.models import Sum
from django.conf import settings
from artwork.models import Artwork
from django_countries.fields import CountryField


# Create your models here.
class StoreConfiguration(models.Model):
    """
    Allows admins to dynamically change delivery rules
    via the Django Admin panel.
    """
    free_shipping_threshold = models.DecimalField(
        max_digits=6, decimal_places=2, default=50.00
    )
    standard_delivery_percentage = models.DecimalField(
        max_digits=5, decimal_places=2, default=10.00
    )

    class Meta:
        verbose_name_plural = "Store Configuration"

    def __str__(self):
        return "Global Store Configuration"


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

    def _generate_order_number(self):
        """
        Generate random unique order number using uuid
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time a line item is added,
        accounting for shipping costs.
        """
        # Sums up all the line item totals linked to this specific order
        self.order_total = self.lineitems.aggregate(
            Sum('lineitem_total'))['lineitem_total__sum'] or 0

        # this section of code will get the threshold for discount
        # as well as the discount percentage if admin changes it
        config = StoreConfiguration.objects.first()
        threshold = config.free_shipping_threshold if config else 50.00
        percentage = config.standard_delivery_percentage if config else 10.00

        # the shipping cost calculation
        if self.order_total < threshold:
            self.shipping_cost = self.order_total * (percentage / 100)
        else:
            self.shipping_cost = 0

        self.grand_total = self.order_total + self.shipping_cost
        super().save(
            update_fields=['order_total', 'shipping_cost', 'grand_total']
            )

    def save(self, *args, **kwargs):
        """
        If the ordernumber is not set
        example by changing details
        this function will set it
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

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

    def save(self, *args, **kwargs):
        """
        Automatically calculate the line item total on save,
        then trigger the parent order to update its grand total.
        """
        self.lineitem_total = self.artwork.price * self.quantity
        super().save(*args, **kwargs)
        self.order.update_total()

    def __str__(self):
        """
        Returns a recognizable label for the admin panel
        """
        return (
            f'"{self.artwork.title}" by {self.artwork.artist.name} '
            f'on order {self.order.order_number}'
        )
