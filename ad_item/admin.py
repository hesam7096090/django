from django.contrib import admin
from .models import *
from .views import *



admin.site.register(Category)
admin.site.register(Item)