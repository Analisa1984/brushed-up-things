from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from artwork.models import Artwork


# Create your views here.
def shopping_cart(request):
    """this function will render the shopping bag contents page"""
    cart = request.session.get('cart', {})
    cart_contents = []
    cart_has_sold_items = False

    # Loop through the item IDs currently sitting in the session cart
    for item_id in cart.keys():
        try:
            artwork = Artwork.objects.get(id=item_id)

            # If it was sold while sitting in their cart, attach custom message
            if artwork.is_sold:
                artwork.unavailable_message = (
                    f"'{artwork.title}' was just sold "
                    f"and is no longer available!"
                )
                cart_has_sold_items = True
            cart_contents.append({
                'item_id': item_id,
                'artwork': artwork,
            })
        except Artwork.DoesNotExist:
            continue

    context = {
        'cart_items': cart_contents,
        'cart_has_sold_items': cart_has_sold_items,
    }

    template = 'cart/shopping_cart.html'
    return render(request, template, context)


def add_to_cart(request, item_id):
    """Add artwork pieces to the cart"""
    cart = request.session.get('cart', {})
    # this code makes sure a person cannot add more that one of the item
    # as each art piece is unique and singular
    if item_id in cart:
        messages.info(
            request, "This unique artwork is already in your shopping cart!"
            )
        return redirect(reverse('gallery'))

    cart[item_id] = 1
    request.session['cart'] = cart
    messages.success(request, "Artwork successfully added to your cart!")
    return redirect(reverse('gallery'))


def remove_from_cart(request, item_id):
    """ This remove single specific items in the shopping cart"""
    try:
        cart = request.session.get('cart', {})

        if item_id in cart:
            del cart[item_id]
            messages.success(request, "Item removed from your cart.")

        request.session['cart'] = cart
        return redirect(reverse('shopping_cart'))

    except Exception as e:
        messages.error(request, f"Error removing item: {e}")
        return redirect(reverse('shopping_cart'))


def clear_cart(request):
    """Clear the entire shopping cart"""
    if 'cart' in request.session:
        del request.session['cart']
        messages.success(request, "Your shopping cart has been emptied!")
    else:
        messages.info(request, "Your shopping cart is already empty.")
    return redirect(reverse('shopping_cart'))
