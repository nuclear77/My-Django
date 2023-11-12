from django.contrib import admin
from .models import Item

admin.site.register(Item)

from .models import Image

admin.site.register(Image)

# Register your models here.
