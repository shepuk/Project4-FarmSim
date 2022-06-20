from django.contrib import admin
from .models import Farm


class FarmAdmin(admin.ModelAdmin):
    list_display = (
        'user',
    )

    ordering = ('user',)


admin.site.register(Farm, FarmAdmin)