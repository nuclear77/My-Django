from django.db import models


class Event(models.Model):
    title = models.CharField(max_lenth=200)
    description = models.TextField()
    start_date = models.DateTimeField()
    location = models.CharField(max_length=100)
    registration_open = models.BooleanField(default=True)
    max_attendees = models.PositiveIntegerField(default=100)


    def __str__(self):
        return self.title


class Registration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    attendees_name = models.CharField(max_length=100)
    attendees_email = models.EmailField()
    registration_date = models.DateTimeField(auto_now_add=True)
# Create your models here.
