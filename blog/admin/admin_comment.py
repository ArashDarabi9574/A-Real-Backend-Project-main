from django.contrib import admin
from blog.models.model_blog_post_comment import PostComment


@admin.register(PostComment)
class PostCommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'reply', 'rate')
    search_fields = ('post',)

    fieldsets = (
        (None, {'fields': ('post',)}),
        ("Info User", {'fields': ('user', 'message', 'is_reply', 'rate')}),
        ('Reply', {'fields': ('reply',)}),
    )

    add_fieldsets = (
        (None, {'fields': ('post',)}),
        ("Info User", {'fields': ('user', 'message', 'is_reply', 'rate')}),
        ('Reply', {'fields': ('reply ',)}),
    )
