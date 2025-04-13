from django.contrib import admin
from page.models import BaseInfo


@admin.register(BaseInfo)
class BaseInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'address',)

    fieldsets = (
        ('Main', {'fields': ('name', 'phone_number', 'address', 'logo', 'logo_alt')}),
    )

    add_fieldsets = (
        ('Main', {'fields': ('name', 'phone_number', 'address', 'logo', 'logo_alt')}),
    )
