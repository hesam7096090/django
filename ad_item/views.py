from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ItemForm


from .models import Item, Category

@login_required
def add_item(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.owner = request.user
            item.save()
            return redirect('home:home')  # صفحه‌ای که کاربر به آن منتقل می‌شود
    else:
        form = ItemForm()
    return render(request, 'add_item/add_item.html', {'form': form, 'categories': categories})
