from django import forms
from .models import Item

class ItemFrom(forms.ModelForm):

    class Meta:
        model = Item
        fields = ['name', 'email', 'event']