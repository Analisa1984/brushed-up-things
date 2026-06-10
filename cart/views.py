from django.shortcuts import render, redirect, reverse


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
        return redirect(reverse('gallery'))

    cart[item_id] = 1
    request.session['cart'] = cart
    return redirect(reverse('gallery'))


def remove_from_cart(request, item_id):
    """ This remove single specific items in the shopping cart"""
    try:
        cart = request.session.get('cart', {})

        if item_id in cart:
            del cart[item_id]

        request.session['cart'] = cart
        return redirect(reverse('shopping_cart'))

    except Exception as e:
        return redirect(reverse('shopping_cart'))
