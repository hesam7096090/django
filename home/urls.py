from django.urls import path

from . import views
from .views import *

app_name = 'home'

urlpatterns = [
    path('', home_view, name='home'),
    path('search/', views.search_results, name='search_results'),
]