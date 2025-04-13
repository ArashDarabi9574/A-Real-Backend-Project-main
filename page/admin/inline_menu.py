from django.contrib import admin

from page.models import (
    UpMenu, DownRightMenu, DownLeftMenu, DownMiddleMenu
)


class UpMenuInline(admin.TabularInline):
    model = UpMenu
    extra = 3
    fieldsets = (
        ('Main', {'fields': ('title', 'link', 'description', 'position')}),
    )

    add_fieldsets = (
        ('Main', {'fields': ('title', 'link', 'description', 'position')}),
    )

class DownRightMenuInline(admin.TabularInline):
    model = DownRightMenu
    extra = 3
    fieldsets = (
        ('Main', {'fields': ('title', 'link', 'position')}),
    )

    add_fieldsets = (
        ('Main', {'fields': ('title', 'link', 'position')}),
    )
    
class DownLeftMenuInline(admin.TabularInline):
    model = DownLeftMenu
    extra = 3
    fieldsets = (
        ('Main', {'fields': ('title', 'link', 'position')}),
    )

    add_fieldsets = (
        ('Main', {'fields': ('title', 'link', 'position')}),
    )

class DownMiddleMenuInline(admin.TabularInline):
    model = DownMiddleMenu
    extra = 3
    fieldsets = (
        ('Main', {'fields': ('title', 'link', 'position')}),
    )

    add_fieldsets = (
        ('Main', {'fields': ('title', 'link', 'position')}),
    )