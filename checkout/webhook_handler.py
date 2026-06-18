import time
import json
from django.http import HttpResponse
from .models import Order, OrderLineItem
from artwork.models import Artwork


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unhandled webhook event
        """
        return HttpResponse(
            content=f'Unhandled Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        cart = intent.metadata.cart
        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping

        # Clean shipping data fields to safely match database requirements
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        # Safely extract first and last names out of shipping details
        names = (
            shipping_details.name.split(' ')
            if shipping_details.name
            else ['Anonymous']
        )
        shipping_first_name = names[0]
        shipping_last_name = names[-1] if len(names) > 1 else ''

        order_exists = False
        attempt = 1

        # try 5 times over 5 seconds to see if the view
        # successfully saved the order first.
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    first_name__iexact=shipping_first_name,
                    last_name__iexact=shipping_last_name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    post_code__iexact=shipping_details.address.postal_code,
                    town_or_city__iexact=shipping_details.address.city,
                    street_address1__iexact=shipping_details.address.line1,
                    street_address2__iexact=shipping_details.address.line2,
                    county__iexact=shipping_details.address.state,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)

        if order_exists:
            return HttpResponse(
                content=(
                    f'Webhook received: {event["type"]} | '
                    'SUCCESS: Verified order already in database'
                ),
                status=200)
        else:
            order = None
            try:
                # Fallback if user session died
                order = Order.objects.create(
                    first_name=shipping_first_name,
                    last_name=shipping_last_name,
                    email=billing_details.email,
                    phone_number=shipping_details.phone,
                    country=shipping_details.address.country,
                    post_code=shipping_details.address.postal_code,
                    town_or_city=shipping_details.address.city,
                    street_address1=shipping_details.address.line1,
                    street_address2=shipping_details.address.line2,
                    county=shipping_details.address.state,
                )

                # Reconstruct line items out of the Stripe metadata attachment
                for item_id, quantity in json.loads(cart).items():
                    artwork = Artwork.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        artwork=artwork,
                        quantity=quantity,
                    )
                    order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)

        return HttpResponse(
            content=(
                f'Webhook received: {event["type"]} | '
                'SUCCESS: Created order in webhook'
            ),
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
