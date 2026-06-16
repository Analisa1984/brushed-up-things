/*
    Core logic/payment flow for Stripe Elements - Modern ES6+ Version
*/

// Slice out quotations from the keys passed from Django
const stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
const clientSecret = $('#id_client_secret').text().slice(1, -1);

// Initialize Stripe 
const stripe = Stripe(stripePublicKey);

// Create instance of Stripe UI Elements
const elements = stripe.elements();

// Styling for the card 
const cardStyles = {
    base: {
        color: '#212529', 
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSize: '16px',
        '::placeholder': {
            color: '#6c757d'
        }
    }
};

// Create the Card Element component
const card = elements.create('card', { 
    style: cardStyles,
    hidePostalCode: true
});

// Mount/Inject that component directly into HTML container element
card.mount('#card-element');

//  Handle real-time validation errors on the card Element
card.on('change', function (event) {
    const errorDiv = $('#card-errors');
    if (event.error) {
        errorDiv.text(event.error.message);
    } else {
        errorDiv.text('');
    }
});

// Handle form submission
const form = $('#payment-form');

form.submit(function(ev) {
    ev.preventDefault(); // Stops form from submitting normally
    
    // Disable both the card input and the submit button to prevent double-clicks
    card.update({ 'disabled': true });
    $('#submit-button').attr('disabled', true);

    // Securely confirm the payment with Stripe
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }
    }).then(function(result) {
        if (result.error) {
            // If something went wrong, show the error to the customer
            const errorDiv = $('#card-errors');
            errorDiv.text(result.error.message);
            
            // Re-enable inputs so the user can try again
            card.update({ 'disabled': false });
            $('#submit-button').attr('disabled', false);
        } else {
            // The payment has been processed successfully
            if (result.paymentIntent.status === 'succeeded') {
                form.get(0).submit();  // using get(0) prevents infinite loop
            }
        }
    });
});