from django.contrib import admin
from list.models import List, Item


@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'posted_at', 'price']


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'description', 'image', 'list']
