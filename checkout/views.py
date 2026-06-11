from django.shortcuts import render


# Create your views here.
def checkout(request):
    """this function will render the checkout page"""
    template = 'checkout/checkout.html'
    return render(request, template)
