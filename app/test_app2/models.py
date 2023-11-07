from django.db import models
from django import forms


class Item (models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateTimeField()
    location = models.CharField(max_length=100)
    registration_open = models.BooleanField(default=True)
    max_attendees = models.PositiveIntegerField(default=100)


    def __str__(self):
        return self.title


class RegistrationForm(forms.Form):
    attendee_name = forms.CharField(max_length=100)
    attendee_email = forms.EmailField()
    event = forms.ModelChoiceField(queryset=Item.objects.filter(registration_open=True))
# Create your models here.

