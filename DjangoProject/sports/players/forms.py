from .models import PlayerModel
from django import forms

class PlayerForm(forms.ModelForm):
    class Meta:
        model = PlayerModel
        fields = '__all__'