from models import *
import django_filters


class ItemFilter(django_filters.FilterSet):
    city = django_filters.CharFilter(lookup_expr='icontains')
