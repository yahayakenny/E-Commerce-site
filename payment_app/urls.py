from django.urls import  path
from payment_app import views

urlpatterns = [
   path('payments/', views.payments, name = "payments")
]
