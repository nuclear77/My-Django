from django.contrib import admin
from .models import Item
from .models import Image

admin.site.register(Item)




class CustomAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'price')
    search_fields = ('title',)
    list_display_links = ('image',)

admin.site.register(Image, CustomAdmin)



