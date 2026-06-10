from django.shortcuts import get_object_or_404
from artwork.models import Artwork


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
    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
    }

    return context
