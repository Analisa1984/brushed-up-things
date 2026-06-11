from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    """Allows us to add/edit line items right inside the Order page"""
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = (
        'order_number', 'shipping_cost', 
        'order_total', 'grand_total'
    )

    fields = (
        'order_number', 'first_name', 'last_name', 
        'email', 'phone_number', 'street_address1', 
        'street_address2', 'town_or_city', 'county', 
        'country', 'post_code', 'shipping_cost', 
        'order_total', 'grand_total'
    )

    # This controls what you see on the main list dashboard screen
    list_display = (
        'order_number', 'first_name', 
        'last_name', 'grand_total'
    )

    # Automatically order them by newest first
    ordering = ('-id',)
