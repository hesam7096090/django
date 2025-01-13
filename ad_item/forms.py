from django import forms
from .models import *

# forms.py
from django import forms

from .models import *

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            'category', 'title', 'description', 'quantity_available',
            'province', 'city', 'address', 'collateral_required',
            'collateral_types', 'price_per_day'
        ]
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter item title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter description'}),
            'quantity_available': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter quantity'}),
            'province': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter province'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter city'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter full address'}),
            'collateral_required': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'price_per_day': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter daily price'}),
        }

