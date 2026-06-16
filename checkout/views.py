import stripe
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings
from cart.contexts import cart_contents
from .forms import OrderForm
from .models import Order, OrderLineItem
from artwork.models import Artwork
from django.contrib.auth.decorators import login_required

@login_required
def checkout(request):
    """
    Calculates bag totals, sets up the Stripe Payment Intent,
    and renders the checkout form.
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    # when complete order is clicked
    if request.method == 'POST':
        cart = request.session.get('cart', {})

        form_data = {
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'post_code': request.POST['post_code'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }

        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()     
            # Iterate through cart items to create line items
            for item_id, quantity in cart.items():
                try:
                    artwork = Artwork.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        artwork=artwork,
                        quantity=quantity,
                    )
                    order_line_item.save()
                except Artwork.DoesNotExist:
                    messages.error(request, (
                        "One of the items in your "
                        "cart wasn't found in our database. "
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('shopping_cart'))

            # Save the profile info if they checked the 'save-info' box
            request.session['save_info'] = 'save-info' in request.POST

            # Clears the shopping cart
            if 'cart' in request.session:
                del request.session['cart']

            # Redirect to a success page
            return redirect(
                reverse('checkout_success', args=[order.order_number])
                )
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')

    else:
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(request, "There's nothing in your shopping cart at the moment")
            return redirect(reverse('gallery'))
        current_cart = cart_contents(request)
        grand_total = current_cart['grand_total']
        stripe_total = round(grand_total * 100)
        stripe.api_key = stripe_secret_key

        try:
            intent = stripe.PaymentIntent.create(
                amount=stripe_total,
                currency=settings.STRIPE_CURRENCY,
            )
            client_secret = intent.client_secret
        except Exception as e:
            messages.error(request, f"Stripe error: {e}")
            return redirect(reverse('shopping_cart'))

        # Initialize the Form
        order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(
            request,
            'Stripe public key is missing. Did you forget to set it?'
        )

    if request.method == 'POST':
        client_secret = request.POST.get('client_secret', '')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
     successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. \
        A confirmation email will be sent to {order.email}.')

    # Delete the save_info flag as user clicked save
    if 'save_info' in request.session:
        del request.session['save_info']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
