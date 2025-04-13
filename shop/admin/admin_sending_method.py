from django.contrib import admin
from shop.models import SendingMethod


@admin.register(SendingMethod)
class SendingMethodAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'status', 'free_price')
    search_fields = ('status',)
    ordering = ('-id',)

    fieldsets = (('Main', {'fields': ('title', "description", 'free_price', 'price', 'state', 'status')}),)
    add_fieldsets = (('Main', {'fields': ('title', "description", 'free_price', 'price', 'state', 'status')}),)
