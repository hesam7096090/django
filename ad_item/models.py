from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# models.py
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Item(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    title = models.CharField(max_length=255)
    description = models.TextField()
    quantity_available = models.PositiveIntegerField(default=1)
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    collateral_required = models.BooleanField(default=False)
    collateral_types = models.JSONField(null=True, blank=True)
    province = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    product = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return f"Image for {self.product.title}"
