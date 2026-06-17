from django.shortcuts import get_object_or_404
from decimal import Decimal
from django.conf import settings
from artwork.models import Artwork
from checkout.models import StoreConfiguration


def cart_contents(request):
    """
    A site-wide processor that makes cart data available to all templates
    """
    cart_items = []
    total = 0
    product_count = 0

    # Get the current cart dictionary from the session memory
    cart = request.session.get('cart', {})

    # Loop through each item ID currently inside our cart dictionary
    for item_id, quantity in cart.items():
        # Find the actual artwork in our database using its ID
        artwork = get_object_or_404(Artwork, pk=item_id)
        total += quantity * artwork.price
        product_count += quantity

        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'artwork': artwork,
        })

    config = StoreConfiguration.objects.first()
    threshold = config.free_shipping_threshold if config else Decimal(
        settings.FREE_DELIVERY_THRESHOLD
        )
    percentage = config.standard_delivery_percentage if config else Decimal(
        settings.STANDARD_DELIVERY_PERCENTAGE
        )

    if total < threshold:
        shipping_cost = total * (percentage / Decimal('100'))
    else:
        shipping_cost = Decimal('0.00')

    grand_total = total + shipping_cost

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'shipping_cost': shipping_cost,
        'grand_total': grand_total,
    }

    return context
