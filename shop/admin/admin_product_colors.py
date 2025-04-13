from django.contrib import admin

from shop.models import Colors


@admin.register(Colors)
class ColorsAdmin(admin.ModelAdmin):
    list_display = ('id', 'color_name')

    fieldsets = (
        ('Main', {'fields': ('color_name',)}),
    )

    add_fieldsets = (
        ('Main', {'fields': ('color_name',)}),
    )
