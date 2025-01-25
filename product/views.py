# Create your views here.
from itertools import product
from django.shortcuts import render , redirect
from ad_item.models import *
from django.core.paginator import Paginator
from .forms import *
def product_list(request):
    category_id = request.GET.get('category')
    categories = Category.objects.all()

    if category_id:
        items = Item.objects.filter(category_id=category_id)
    else:
        items = Item.objects.all()

    # اضافه کردن وضعیت ذخیره‌شده برای کاربر جاری
    for item in items:
        item.is_saved = request.user in item.save_item.all()

    paginator = Paginator(items, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'product/products.html', {
        'items': page_obj,
        'categories': categories,
        'selected_category': category_id,
    })


from django.shortcuts import render, get_object_or_404
from .models import *



from datetime import datetime



def product_detail(request, id):
    item = get_object_or_404(Item, id=id)
    collateral_type = item.collateral_types.all()
    total_price = None
    error_message = None

    if request.method == 'POST':
        form = RentalForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            quantity = form.cleaned_data['quantity']

            days = (end_date - start_date).days
            if days > 0:
                if quantity <= item.quantity_available:
                    total_price = days * item.price_per_day * quantity
                else:
                    error_message = "The requested quantity exceeds available stock."
            else:
                error_message = "End date must be after start date."
        else:
            error_message = "Please correct the errors in the form."
    else:
        form = RentalForm()

    return render(request, 'product/detail_product.html', {
        'item': item,
        'collateral_type': collateral_type,
        'form': form,
        'total_price': total_price,
        'error_message': error_message,

    })

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

@login_required
def saved_items(request, id):
    url = request.META.get('HTTP_REFERER', '/')
    item = get_object_or_404(Item, id=id)

    if item.save_item.filter(id=request.user.id).exists():
        item.save_item.remove(request.user)
    else:
        item.save_item.add(request.user)
    return redirect(url)

