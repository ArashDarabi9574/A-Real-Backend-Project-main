from django.contrib import admin

from shop.models import AttributeStyle


@admin.register(AttributeStyle)
class AttributeStyleAdmin(admin.ModelAdmin):
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
