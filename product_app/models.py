from django.db import models

# Create your models here.
from django.db import models
from django.shortcuts import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    product_image = models.ImageField(null = True, blank = True)
    name = models.CharField(max_length=200)
    slug = models.SlugField(default="testing")
    category= models.ForeignKey(Category, on_delete=models.CASCADE)
    product_description= models.CharField(max_length=500, null = True, blank = True)
    price = models.FloatField()

    def __str__(self):
        return self.name

    def get_add_to_cart_url(self):
        return reverse(
            "core:add-to-cart", kwargs={"slug": self.slug}
        )

