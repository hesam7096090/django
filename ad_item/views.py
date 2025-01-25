from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ItemForm
from .models import ProductImage, Collateral


@login_required
def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)

            product.owner = request.user
            product.latitude = request.POST.get('latitude')
            product.longitude = request.POST.get('longitude')

            product.save()
            form.save_m2m()

            images = request.FILES.getlist('images')
            for image in images:
                ProductImage.objects.create(product=product, image=image)

            return redirect('home:home')
    else:
        form = ItemForm()

    collaterals = Collateral.objects.all()
    return render(
        request,
        'add_item/add_item.html',
        {'form': form, 'collaterals': collaterals}
    )
