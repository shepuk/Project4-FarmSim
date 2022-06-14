from django.contrib import admin
from .models import Profile, Inventory


class InventoryAdmin(admin.ModelAdmin):
    list_display = (
        'owner',
        'item',
        'quantity',
    )

    ordering = ('owner',)


admin.site.register(Profile)
admin.site.register(Inventory, InventoryAdmin)
