
from django.contrib import admin
from accounts.models import UserAddress


class AddressInline(admin.TabularInline):
    model = UserAddress
    extra = 3
    fieldsets = (
        ('Main', {'classes': ('collapse',), 'fields': (
            'postal_code', 'province', 'city', 'address', 'plaque', 'telephone_number', 'reciever')}),
    )
    fieldsets_add = (
        ('Main', {'classes': ('collapse',), 'fields': (
            'postal_code', 'province', 'city', 'address', 'plaque', 'telephone_number', 'reciever')}),
    )
