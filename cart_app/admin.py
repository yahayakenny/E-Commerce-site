from django.contrib import admin
from cart_app.models import Cart, Order

# Register your models here.
admin.site.register(Cart)
admin.site.register(Order)