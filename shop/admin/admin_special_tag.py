from django.contrib import admin
from shop.models import SpecialTag


@admin.register(SpecialTag)
class SpecialTagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'color')
    ordering = ['-id']
    search_fields = (
        'id', 'title',
    )
    fieldsets = (
        ('Main', {'fields': ('title', 'color')}),
    )

    add_fieldsets = (
        ('Main', {'fields': ('title', 'color')}),
    )
