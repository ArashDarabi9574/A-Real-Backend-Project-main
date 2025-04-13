from django.contrib import admin
from model_clone import CloneModelAdmin

from page.models import LandingPage
from page.admin.inline_slider_icons import (
    SliderInline,
    IconsInline,
    UnderSliderInline
)
from page.admin.inline_menu import (
    UpMenuInline,
    DownRightMenuInline,
    DownLeftMenuInline,
    DownMiddleMenuInline
)

@admin.register(LandingPage)
class LandingPageAdmin(CloneModelAdmin):
    list_display = ('id', 'landing_page_name')
    search_fields = ('id',)
    inlines = [SliderInline, IconsInline, UnderSliderInline,
               UpMenuInline, DownRightMenuInline, DownLeftMenuInline, DownMiddleMenuInline]

    fieldsets = (
        ('تصویر پایین', {'fields': ('landing_page_name',
         'button_image', 'button_image_alt', 'button_link')}),
        ('لینک دسترسی سریع', {'fields': ('quick_access_name',
         'quick_access_link',)}),

         ('پیشنهاد ویژه', {'fields': (
             'special_link_1', 'special_image_1', 'special_title_1', 'special_desc_1',
             'special_link_2', 'special_image_2', 'special_title_2', 'special_desc_2',
             'special_link_3', 'special_image_3', 'special_title_3', 'special_desc_3',
             )}),
    )

    add_fieldsets = (
        ('تصویر پایین', {'fields': ('landing_page_name',
         'button_image', 'button_image_alt', 'button_link')}),
        ('لینک دسترسی سریع', {'fields': ('quick_access_name',
         'quick_access_link',)}),

        ('پیشنهاد ویژه', {'fields': (
             'special_link_1', 'special_image_1', 'special_title_1', 'special_desc_1',
             'special_link_2', 'special_image_2', 'special_title_2', 'special_desc_2',
             'special_link_3', 'special_image_3', 'special_title_3', 'special_desc_3',
             )}),
    )
