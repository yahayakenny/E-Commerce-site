from django.urls import  path
from checkout_app import views

urlpatterns = [
   path('checkout/', views.checkout, name = "checkout")
]
