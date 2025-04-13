from django.contrib import admin

from shop.models import Brand


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug',  'country',
                    'position', 'guarantee', 'guarantee_conditions')
    search_fields = (
        'id', 'title', 'slug',
    )
    list_filter = ('country',)
    ordering = ['-id', ]

    fieldsets = (
        ('Main', {'fields': ('title', 'description', 'position',
         'slug', 'country', 'thumbnail', 'thumbnail_alt', 'guarantee', 'guarantee_conditions')}),
    )

    add_fieldsets = (
        ('Main', {'fields': ('title', 'description', 'position',
         'slug', 'country', 'thumbnail', 'thumbnail_alt', 'guarantee', 'guarantee_conditions')}),
    )
