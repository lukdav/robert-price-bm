from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, 'There is nothing in your shopping bag')
        return redirect(reverse('products'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KFmbgD3SFldYSV5AWapWc9Ik9mupEk0SYhRUN08WfzSyeikQtd1x1Qsv7cFwX8pi5FoYJBDsmr9OGvMEbejv8qF00BDwvoSoz',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
