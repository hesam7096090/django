

# Create your views here.
from django.shortcuts import render
from ad_item.models import *

def product_list(request):
    category_id = request.GET.get('category')  # دریافت آیدی دسته‌بندی از URL
    categories = Category.objects.all()  # لیست همه دسته‌بندی‌ها
    if category_id:
        items = Item.objects.filter(category_id=category_id)  # فیلتر محصولات بر اساس دسته‌بندی
    else:
        items = Item.objects.all()  # نمایش همه محصولات

    return render(request, 'product/products.html', {'items': items, 'categories': categories, 'selected_category': category_id})
