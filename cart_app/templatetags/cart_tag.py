from django import template
from cart_app.models import Order

register = template.Library()

@register.filter
def cart_total(user):
    orders = Order.objects.filter(user=user, ordered=False)
    order = orders[0]
    print(len(orders))
    print(order.orderitems.all())

    total = sum([item.quantity for item in order.orderitems.all()])
    
    return total

