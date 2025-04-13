from django.contrib import admin

from page.models import (
    Slider,
    Icons,
    UnderSlider
)


class SliderInline(admin.TabularInline):
    model = Slider
    extra = 3
    fieldsets = (
        ('Main', {'fields': ('slider_link', 'slider_image', 'slider_image_alt', 'position')}),
    )

    add_fieldsets = (
        ('Main', {'fields': ('slider_link', 'slider_image', 'slider_image_alt', 'position')}),
    )


class IconsInline(admin.TabularInline):
    model = Icons
    extra = 7
    fieldsets = (
        ('Main', {'fields': ('icon_name', 'icon_link',
         'icon_thumbnail', 'icon_thumbnail_alt', 'position')}),
    )

    add_fieldsets = (
        ('Main', {'fields': ('icon_name', 'icon_link',
         'icon_thumbnail', 'icon_thumbnail_alt', 'position')}),
    )


class UnderSliderInline(admin.TabularInline):
    model = UnderSlider
    extra = 2
    fieldsets = (
        ('Main', {'fields': ('under_slider_image', 'under_slider_link',
         'under_slider_image_alt', 'position')}),
    )

    add_fieldsets = (
        ('Main', {'fields': ('under_slider_image', 'under_slider_link',
         'under_slider_image_alt', 'position')}),
    )
