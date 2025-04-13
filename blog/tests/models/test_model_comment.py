import tempfile

from django.test import TestCase
from django.contrib.auth import get_user_model
from blog.models import Post, PostCategory, PostComment


class CommentModelTestCase(TestCase):
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

        self.replay = PostComment.objects.create(
            name='replay admin',
            email='admin@gmail.com',
            message='reply admin admin',

            rate=1,
            post=self.post
        )

        self.comment = PostComment.objects.create(
            name='admin',
            email='admin@gmail.com',
            message='admin admin admin',
            post=self.post,

            rate=1,
            reply=self.replay
        )

    def test_method_str_comment(self):
        self.assertTrue(self.comment)
        self.assertEquals(str(self.comment), 'admin')

    def test_method_str_reply(self):
        self.assertTrue(self.replay)
        self.assertEquals(str(self.replay), 'replay admin')

    def test_fields_model_comment(self):
        self.assertTrue(self.comment.status)
        self.assertIsNotNone(self.comment.post)
        self.assertIsNotNone(self.comment.reply)
        self.assertFalse(self.comment.is_active)
        self.assertIsNotNone(self.comment.created_at)
        self.assertEquals(self.comment.email, 'admin@gmail.com')
        self.assertEquals(self.comment.message, 'admin admin admin')
        self.assertEquals(self.comment.rate, 1)

    def test_fields_model_replay(self):
        self.assertTrue(self.replay.status)
        self.assertIsNotNone(self.replay.post)
        self.assertFalse(self.replay.is_active)
        self.assertIsNotNone(self.replay.created_at)
        self.assertEquals(self.replay.email, 'admin@gmail.com')
        self.assertEquals(self.replay.message, 'reply admin admin')
        self.assertEquals(self.comment.rate, 1)
