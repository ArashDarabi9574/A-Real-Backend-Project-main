from django.contrib import admin

from shop.models import Gallery


class GalleryInline(admin.TabularInline):
    model = Gallery
    extra = 10
    fieldsets = (
        ('Main', {'fields': ('image', 'image_alt')}),
    )

    add_fieldsets = (
        ('Main', {'fields': ('image', 'image_alt')}),
    )
