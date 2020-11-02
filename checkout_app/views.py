from django.shortcuts import render
from .forms import BillingForm
from cart_app.models import Order
from checkout_app.models import Billing

# Create your views here.
def checkout(request):
    order_qs = Order.objects.filter(user= request.user, ordered=False)
    order_items = order_qs[0].orderitems.all()
    order_total = order_qs[0].get_totals()

    form = BillingForm()
    if request.method == 'POST':
        form = BillingForm(request.POST or None)
        if form.is_valid():
            get_number = form.cleaned_data.get('phone')
            get_email = form.cleaned_data.get('email')
            print(get_number)
            print(get_email)
            form.save()

    return render (request, 'checkout/checkout.html', {'form': form, "order_items": order_items, "order_total": order_total})
