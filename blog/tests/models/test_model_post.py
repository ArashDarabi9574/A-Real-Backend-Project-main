import tempfile

from django.contrib.auth import get_user_model
from django.test import TestCase
from blog.models import Post, PostCategory


class PostModelTestCase(TestCase):
    def setUp(self) -> None:
        self.category = PostCategory.objects.create(
            title='category fake',
            description='description fake',
        )

        self.author = get_user_model().objects.create(
            username='author',
            password='author123123',
        )

        self.post = Post.objects.create(
            title='post fake',
            content='content fake',
            author=self.author,
            category=self.category,
            thumbnail=tempfile.NamedTemporaryFile(suffix='.jpg').name
        )

    def test_method_str_post(self):
        self.assertTrue(self.post)
        self.assertEquals(str(self.post), 'post fake')

    def test_auto_generate_slug_post(self):
        self.assertTrue(self.post.slug)
        self.assertEquals(self.post.slug, 'post-fake')
        self.assertNotEquals(self.post.slug, 'sub-category-fake')

    def test_auto_generate_thumbnail_alt_post(self):
        self.assertTrue(self.post.thumbnail_alt)
        self.assertEquals(self.post.thumbnail_alt, 'post-fake')
        self.assertNotEquals(self.post.thumbnail_alt, 'sub-category-fake')

    def test_fields_model_post(self):
        self.assertTrue(self.post.status)
        self.assertFalse(self.post.is_active)
        self.assertEquals(self.post.content, 'content fake')
        self.assertTrue(self.post.thumbnail)
        self.assertIsNotNone(self.post.category)
        self.assertIsNotNone(self.post.author)
        self.assertIsNotNone(self.post.created_at)
