from django import forms
from .models import customersDetailsModel


class customerDetailForm(forms.ModelForm):
    class Meta:
        model = customersDetailsModel
        fields = '__all__'
