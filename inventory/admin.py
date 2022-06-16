from django.contrib import admin
from .models import Inventory


class InventoryAdmin(admin.ModelAdmin):
    list_display = (
        'owner',
        'item',
        'quantity',
    )

    ordering = ('owner',)


admin.site.register(Inventory, InventoryAdmin)
