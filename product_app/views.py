from django.shortcuts import render
from product_app.models import Product


# Create your views here.

def home(request):
    products = Product.objects.all
    return render(request,
     'products/index.html',
      {'products': products})

def product_detail(request, slug):
    product = Product.objects.get(id = slug)
    return render (
        request,
        'products/product_detail.html',
        {'product': product}
    )
