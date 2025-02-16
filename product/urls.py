from django.urls import path
from . import views



app_name = 'product'
urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product_detail/<int:id>/', views.product_detail, name='product_detail'),
    path('saved_items/<int:id>/', views.saved_items, name='saved_products'),
]
