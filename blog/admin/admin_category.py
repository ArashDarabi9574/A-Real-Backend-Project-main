from django.contrib import admin
from blog.models.model_blog_post_category import PostCategory


@admin.register(PostCategory)
class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'get_created_at_jalali',)
    search_fields = ('title',)

    fieldsets = (
        ("Main", {'fields': ('title', )}),
    )

    add_fieldsets = (
        ("Main", {'fields': ('title', )}),
    )
