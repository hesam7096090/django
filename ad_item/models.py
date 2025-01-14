from datetime import timezone

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
    item_value = models.PositiveIntegerField(default=0)
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    province = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True , null=True , blank=True)
    address = models.TextField()
    collateral_required = models.BooleanField(default=False)
    collateral_types = models.ManyToManyField('Collateral', blank=True)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True )
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='items', null=True, blank=True , default=1)  # تغییر به null=True

    def __str__(self):
        return self.title





class Collateral(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
