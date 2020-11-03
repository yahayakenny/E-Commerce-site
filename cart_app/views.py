from django.shortcuts import render, get_object_or_404,redirect
from cart_app.models import Cart, Order
from product_app.models import Product
from django.contrib import messages


# Create your views here.
def add_to_cart(request, slug):
    item = get_object_or_404(Product, slug = slug)
    order_item, created = Cart.objects.get_or_create(
        item = item,
        user = request.user
    )
    order_qs = Order.objects.filter(user = request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.orderitems.filter(item__slug = item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, 'Your shopping cart was updated')
            return redirect('home')
        else: 
            order.orderitems.add(order_item)
            messages.info(request, 'This item was added to your cart')
            return redirect('home')
    else:
        order = Order.objects.create(
            user=request.user)
        order.orderitems.add(order_item)
        messages.info(request, "This item was added to your cart.")
        return redirect("home")

    


def remove_from_cart(request, slug):
    item = get_object_or_404(Product, slug = slug)
    cart_qs = Cart.objects.filter(
        user = request.user,
        item = item
)
    order_qs = Order.objects.filter(user = request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.orderitems.filter(item__slug=item.slug).exists():
            order_item = Cart.objects.filter(
                user = request.user,
                item = item
            )[0]
            if order_item.quantity > 1:    
                order_item.quantity -= 1
                order_item.save()
                messages.info(request, 'This item was removed from your cart')
                return redirect('home')

            else:
                cart_qs.delete()
                messages.info(request, 'This item is not in your cart')
                return redirect('home') 
        
        else:
            messages.info(request, 'You do not have an active order')
            return redirect('home')


def cart(request):
    user = request.user
    carts = Cart.objects.filter(
        user=user
        )
    orders = Order.objects.filter(
        user=user,
        ordered=False)

    if carts.exists():
        order = orders[0]
        return render(request, 'cart/cart.html', {"carts": carts, 'order': order})
		
    else:
        messages.warning(request, "You do not have an active order")
        return redirect("home")