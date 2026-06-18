import stripe
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings
from cart.contexts import cart_contents
from .forms import OrderForm
from .models import Order, OrderLineItem
from artwork.models import Artwork
from profiles.models import UserProfile
from django.contrib.auth.decorators import login_required


@login_required
def checkout(request):
    """
    Calculates bag totals, sets up the Stripe Payment Intent,
    and renders the checkout form. Pre-fills fields if a user
    profile exists.
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    # when complete order is clicked
    if request.method == 'POST':
        cart = request.session.get('cart', {})

        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order = order_form.save(commit=False)

            # Link order to user's profile automatically
            profile = get_object_or_404(UserProfile, user=request.user)
            order.user_profile = profile
            order.save()

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

            # Save the profile info flag if they checked the 'save-info' box
            request.session['save_info'] = 'save-info' in request.POST

            # Clears the shopping cart
            if 'cart' in request.session:
                del request.session['cart']

            # Redirect to success page
            return redirect(
                reverse('checkout_success', args=[order.order_number])
            )
        else:
            messages.error(
                request,
                'There was an error with your form. '
                'Please double check your information.'
            )
            # Re-fetch structural cart summary info
            # to prevent template render errors
            current_cart = cart_contents(request)
            client_secret = request.POST.get('client_secret', '')

            template = 'checkout/checkout.html'
            context = {
                'order_form': order_form,
                'stripe_public_key': stripe_public_key,
                'client_secret': client_secret,
            }
            return render(request, template, context)

    else:
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(
                request, "There's nothing in your shopping cart at the moment"
            )
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

        # Initialize the Form with pre-filled UserProfile metrics
        profile = get_object_or_404(UserProfile, user=request.user)
        order_form = OrderForm(initial={
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'email': request.user.email,
            'phone_number': profile.default_phone_number,
            'country': profile.default_country,
            'post_code': profile.default_postcode,
            'town_or_city': profile.default_town_or_city,
            'street_address1': profile.default_street_address1,
            'street_address2': profile.default_street_address2,
            'county': profile.default_county,
        })

    if not stripe_public_key:
        messages.warning(
            request,
            'Stripe public key is missing. Did you forget to set it?'
        )

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handles successful checkouts and saves customer delivery details
    to their profile if 'save_info' is active.
    """
    order = get_object_or_404(Order, order_number=order_number)

    # get profile and check if user elected to overwrite saved delivery
    profile = get_object_or_404(UserProfile, user=request.user)
    save_info = request.session.get('save_info')

    if save_info:
        profile.default_phone_number = order.phone_number
        profile.default_country = order.country
        profile.default_postcode = order.post_code
        profile.default_town_or_city = order.town_or_city
        profile.default_street_address1 = order.street_address1
        profile.default_street_address2 = order.street_address2
        profile.default_county = order.county
        profile.save()

    messages.success(
        request, f'Order successfully processed! '
        f'Your order number is {order_number}. '
        f'A confirmation email will be sent to {order.email}.'
        )

    # Delete the save_info flag as user clicked save
    if 'save_info' in request.session:
        del request.session['save_info']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
