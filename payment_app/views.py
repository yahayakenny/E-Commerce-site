from django.shortcuts import render
from django.conf import settings
from cart_app.models import Cart, Order
from product_app.models import Product
from checkout_app.forms import BillingForm

def payments(request):
    form = BillingForm()
    filled_form = BillingForm(request)
    
    order_qs = Order.objects.filter(ordered=False)
    order_total = order_qs[0].get_totals()

    if request.method == 'POST':
        form = BillingForm(request.POST or None)
        if form.is_valid():
            get_number = form.cleaned_data.get('phone')
            get_email = form.cleaned_data.get('email')
            form.save()

    context = {
        'key': settings.RAVE_PUBLIC_KEY,
        'order_total': order_total,
        'get_number': get_number,
        'get_email': get_email
    }
    return render(request, 'payments/payments.html', context)