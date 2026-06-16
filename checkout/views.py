import stripe
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings
from cart.contexts import cart_contents
from .forms import OrderForm


def checkout(request):
    """
    Calculates bag totals, sets up the Stripe Payment Intent,
    and renders the checkout form.
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('artworks'))

    # get the precalculated current cart  from the context processor
    current_cart = cart_contents(request)
    grand_total = current_cart['grand_total']

    stripe_total = round(grand_total * 100)
    stripe.api_key = stripe_secret_key

    # 2. Handshake with Stripe
    try:
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )
    except Exception as e:
        messages.error(request, f"Stripe error: {e}")
        return redirect(reverse('view_bag'))

    # 3. Initialize the Form
    order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(
            request,
            'Stripe public key is missing. Did you forget to set it?'
        )

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)
