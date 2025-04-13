from django.contrib.auth import get_user_model
from django.test import TestCase
from page.models import Page


class PageTestCase(TestCase):
    def setUp(self) -> None:
        self.author = get_user_model().objects.create(
            username='author fake',
        )
        self.author.set_password('author123123')
        self.author.save()

        self.obj = Page.objects.create(
            title='title fake',
            content='content fake',
            author=self.author,
            status='PU',
        )

    def test_str_method(self):
        self.assertIsNotNone(str(self.obj))
        self.assertEqual(str(self.obj), 'title fake')
        self.assertNotEqual(str(self.obj), 'admin@gmail.com')

    def test_generate_auto_slug(self):
        self.assertTrue(self.obj.slug)
        self.assertEqual(self.obj.slug, 'title-fake')

    def test_generate_auto_thumbnail_alt(self):
        self.assertTrue(self.obj.thumbnail_alt)
        self.assertEqual(self.obj.thumbnail_alt, 'title-fake')

    def test_fields_model(self):
        self.assertTrue(self.obj.status)
        self.assertTrue(self.obj.created_at)
        self.assertNotEqual(self.obj.status, 'PE')
        self.assertEqual(self.obj.author, self.author)
        self.assertEqual(self.obj.content, 'content fake')

    def test_author_page(self):
        self.assertEqual(self.obj.author.username, 'author fake')
        self.assertTrue(self.obj.author.password)
