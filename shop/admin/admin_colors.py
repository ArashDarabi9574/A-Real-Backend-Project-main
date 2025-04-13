from django.contrib import admin

from shop.models import Colors


@admin.register(Colors)
class ColorsAdmin(admin.ModelAdmin):
    list_display = ('id', 'color_name',)
    ordering = ['-id', ]

    fieldsets = (
        ('Main', {'fields': ('color_name', 'color')}),
    )

    add_fieldsets = (
        ('Main', {'fields': ('color_name', 'color')}),
    )
