from django.contrib import admin

from shop.models.model_comment import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('products', 'rate', 'user', 'status')
    search_fields = ('products', 'user',)
    ordering = ['-id', ]
    search_fields = ('id', 'products__title')
    fieldsets = (
        (None, {'fields': ('products', "status",)}),
        ("Info User", {'fields': ('user', 'rate', 'message',)}),
    )

    add_fieldsets = (
        (None, {'fields': ('products', "status",)}),
        ("Info User", {'fields': ('user', 'rate', 'message',)}),
    )
