from django.urls import  path
from cart_app import views

urlpatterns = [
   path('home/add_to_cart/<slug>', views.add_to_cart, name = 'add-to-cart'),
   path('home/remove_from_cart/<slug>', views.remove_from_cart, name = 'remove_from_cart'),
   path('cart/', views.cart, name = "cart")
]
