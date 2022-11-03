from django.contrib import admin

from .models import Purchase, Item

admin.site.register(Item)
admin.site.register(Purchase)


