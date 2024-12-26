from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from ad_item.models import Item
from .models import *


def home_view(request):
  # نمایش ۶ آیتم برتر
    return render(request, 'home/home.html', {

    })

from django.shortcuts import render

def search_results(request):
    query = request.GET.get('q')
    items = Item.objects.filter(title__icontains=query) if query else []
    return render(request, 'home/search_result.html', {'query': query, 'items': items})
