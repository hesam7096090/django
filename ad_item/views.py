from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ItemForm


from .models import *

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

@login_required
def add_item(request):
    if request.method == 'POST':
        collateral = request.POST.getlist('collateral')
        form = ItemForm(request.POST)
        files = request.FILES.getlist('images')
        if form.is_valid():
            product = form.save()
            for file in files:
                ProductImage.objects.create(product=product, image=file)
            return redirect('home:home')  # تغییر به URL مناسب
    else:
        form = ItemForm()
    return render(request, 'add_item/add_item.html', {'form': form})
