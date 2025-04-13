from django.contrib import admin
from blog.models.model_blog_post import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', "author", 'slug',
                    'status', 'get_created_at_jalali',)
    search_fields = ('title', 'slug', 'author')

    fieldsets = (
        ("Main", {'fields': ('title', 'slug', 'thumbnail', 'thumbnail_alt',
         'author', 'category', 'content', 'short_description')}),
        ("SEO information", {'fields': ("meta_title", "meta_description")}),
        ('Settings', {'fields': ('status',)}),
    )

    add_fieldsets = (
        ("Main", {'fields': ('title', 'slug', 'thumbnail', 'thumbnail_alt',
         'author', 'category', 'content', 'short_description')}),
        ("SEO Information", {'fields': ("meta_title", "meta_description")}),
        ('Settings', {'fields': ('status',)}),
    )
