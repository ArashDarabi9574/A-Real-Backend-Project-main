from django.contrib import admin

from shop.models import ProductsCollections


@admin.register(ProductsCollections)
class ProductsCollectionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',  'slug', 'position', 'child_position')
    search_fields = (
        'id', 'title', 'slug',
    )
    ordering = ['-id', ]
    list_filter = ['parent',]
    fieldsets = (
        ('Main', {'fields': ('title', 'slug',
         'parent', 'position', 'child_position')}),
    )

    add_fieldsets = (
        ('Main', {'fields': ('title', 'slug',
         'parent', 'position', 'child_position')}),
    )
