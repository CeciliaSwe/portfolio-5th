from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def payment(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "You do not have anything in your bag!")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'payment/payment.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Kj2IqFllzp5Rb0ietzGEKoTC2Tlpp8y1WNSkYS44YzEsi8lCBDVq1MJ3SGUAWp9lGVM9kI0PZuk7toWcPCMN3IO00qQKsVQ8j',
        'client_secret': 'test client secret',

    }

    return render(request, template, context)