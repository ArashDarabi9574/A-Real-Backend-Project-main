# from modeltranslation.translator import register, TranslationOptions, translator
# from blog.models import PostCategory, PostComment
# from blog.models.model_blog_post import Post


# @register(PostCategory)
# class PostCategoryTranslationOptions(TranslationOptions):
#     fields = ('title', 'description', 'parent_category', 'status', 'is_active','meta_title','meta_description')


# @register(Post)
# class PostTranslationOptions(TranslationOptions):
#     fields = ('title', 'content', 'category', 'status', 'is_active','meta_title','meta_description')


# @register(PostComment)
# class PostCommentTranslationOptions(TranslationOptions):
#     fields = ('post', 'reply', 'name', 'message', 'is_active')
