from django import forms
from .models import Event

class RegistrationForm(forms.Form):
    attendee_name = forms.CharField(label='Your Name', max_length=100)
    attendee_email = forms.EmailField(label='Your Email')
    event = forms.ModelChoiceField(queryset=Event.objects.filter(registration_open=True), label='Select Event')