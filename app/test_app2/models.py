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

class Image(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.title