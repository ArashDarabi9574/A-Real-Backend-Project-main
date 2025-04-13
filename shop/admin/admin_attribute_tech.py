from django.contrib import admin

from shop.models import AttributeTech


@admin.register(AttributeTech)
class AttributeTechAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'position')
    ordering = ['-id', ]
    search_fields = (
        'id', 'title',
    )
    fieldsets = (
        ('Main', {'fields': ('title', 'position')}),
    )

    add_fieldsets = (
        ('Main', {'fields': ('title', 'position')}),
    )
