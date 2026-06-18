from django.shortcuts import render, redirect, reverse
from django.contrib import messages


# Create your views here.
def shopping_cart(request):
    """this function will render the shopping bag contents page"""
    template = 'cart/shopping_cart.html'
    return render(request, template)


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
