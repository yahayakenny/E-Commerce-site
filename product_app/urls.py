from django.urls import  path
from product_app import views

urlpatterns = [
     path('', views.home, name = 'home'),
     path('home/<slug>', views.product_detail, name = 'product_detail')
]
