from django import forms
from datetime import date


class RentalForm(forms.Form):
    start_date = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        label="تاریخ شروع",
    )
    end_date = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        label="تاریخ پایان",
    )
    quantity = forms.IntegerField(
        min_value=1,
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        label="تعداد",
    )

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")
        quantity = cleaned_data.get("quantity")

        if start_date and end_date:
            if start_date > end_date:
                raise forms.ValidationError("تاریخ پایان نمی‌تواند قبل از تاریخ شروع باشد.")

        if quantity and quantity <= 0:
            raise forms.ValidationError("تعداد باید حداقل ۱ باشد.")

        return cleaned_data
