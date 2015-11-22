from django.contrib import admin
from list.models import List, Item, Pledge


@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'posted_at', 'price', 'deadline',
                    'inactive']


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'description', 'image', 'list',
                    'reserved', 'item_link']


@admin.register(Pledge)
class PledgeAdmin(admin.ModelAdmin):
    list_display = ['user', 'item', 'amount', 'charge', 'pledge_time']