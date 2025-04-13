# Core Django
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

# My App
from forms.models import ContactUs


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('id', "name", 'email', 'phone_number', 'created_at', 'updated_at')
    search_fields = ('id', 'name', 'email', 'phone_number')
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        (_('Main'), {'fields': ('name', 'message', 'email', 'phone_number')}),
        (_("Date"), {'fields': ('created_at', "updated_at")}),
    )

    add_fieldsets = (
        (_('Main'), {'fields': ('name', 'message', 'email', 'phone_number')}),
    )
