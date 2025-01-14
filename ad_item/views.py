from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import *


from .models import *

from django.http import HttpResponse
from .models import *

@login_required
def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.save()
            form.save_m2m()  # ذخیره ManyToMany
            images = request.FILES.getlist('images')
            for image in images:
                ProductImage.objects.create(product=product, image=image)
            return redirect('home:home')
    else:
        form = ItemForm()


    collaterals = Collateral.objects.all()  # دریافت موارد وثیقه از دیتابیس
    return render(request, 'add_item/add_item.html', {'form': form, 'collaterals': collaterals})
