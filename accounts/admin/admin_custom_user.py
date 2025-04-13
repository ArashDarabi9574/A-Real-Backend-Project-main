from django.contrib import admin
from django.contrib.auth import get_user_model
from accounts.admin.inline_address import AddressInline
from accounts.models import UserPermission

@admin.register(UserPermission)
class UserPermissionAdmin(admin.ModelAdmin):
    pass

@admin.register(get_user_model())
class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'phone_number', 'email', 'full_name', 'is_staff', 'is_active', 'national_number',
        'is_superuser', 'is_verify', 'get_verify_date',
    )
    search_fields = ('id', 'phone_number', 'email',
                     'first_name', 'last_name', 'national_number')
    list_filter = ('is_staff', 'is_active', 'is_superuser', 'is_verify', 'user_permissions')
    readonly_fields = ('date_joined', 'last_login', 'verify_date')
    inlines = [AddressInline,]
    fieldsets = (
        ('Join', {'classes': ('collapse',), 'fields': (
            'date_joined',)}),
        ('Main', {'classes': ('collapse',), 'fields': (
            'phone_number', 'email', 'national_number',
            'first_name', 'last_name', 'address')}),
        ('Permission', {'classes': ('collapse',), 'fields': (
            'permissions', 'is_staff', 'is_active', 'is_superuser', 'is_verify')}),
        ('Date', {'classes': ('collapse',), 'fields': (
            'last_login', 'verify_date')}),
    )

    fieldsets_add = (
        ('Main', {'classes': ('collapse',), 'fields': (
            'phone_number', 'email', 'password', 'national_number',
            'first_name', 'last_name')}),
        ('Permission', {'classes': ('collapse',), 'fields': (
            'permissions', 'is_staff', 'is_active', 'is_superuser', 'is_verify')}),
        ('Date', {'classes': ('collapse',), 'fields': (
            'date_joined', 'last_login', 'verify_date')}),
    )
