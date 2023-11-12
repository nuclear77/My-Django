from django import forms
from .models import Item

class ItemFrom(forms.ModelForm):

    class Meta:
        model = Item
        fields = ['title']

class UserForm(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField()


