from django.test import TestCase
from blog.models import PostCategory


class CategoryModelTestCase(TestCase):
    def setUp(self) -> None:
        self.sub_category = PostCategory.objects.create(
            title='sub category fake',
            description='sub description fake',
        )

        self.category = PostCategory.objects.create(
            title='category fake',
            description='description fake',
            parent_category=self.sub_category
        )

    def test_method_str_category(self):
        self.assertTrue(self.category)
        self.assertEquals(str(self.category), 'category fake')

    def test_method_str_sub_category(self):
        self.assertTrue(self.sub_category)
        self.assertTrue(str(self.sub_category), 'sub category fake')

        self.assertEquals(str(self.category), 'category fake')
        self.assertEquals(str(self.sub_category), 'sub category fake')

    def test_auto_generate_slug_category(self):
        self.assertTrue(self.category.slug)
        self.assertEquals(self.category.slug, 'category-fake')
        self.assertNotEquals(self.category.slug, 'sub-category-fake')

    def test_auto_generate_slug_sub_category(self):
        self.assertTrue(self.sub_category.slug)
        self.assertEquals(self.sub_category.slug, 'sub-category-fake')
        self.assertNotEquals(self.sub_category.slug, 'category-fake')

    def test_auto_generate_thumbnail_alt_category(self):
        self.assertTrue(self.category.thumbnail_alt)
        self.assertEquals(self.category.thumbnail_alt, 'category-fake')
        self.assertNotEquals(self.category.thumbnail_alt, 'sub-category-fake')

    def test_auto_generate_thumbnail_alt_sub_category(self):
        self.assertTrue(self.sub_category.thumbnail_alt)
        self.assertEquals(self.sub_category.thumbnail_alt, 'sub-category-fake')
        self.assertNotEquals(self.sub_category.thumbnail_alt, 'category-fake')

    def test_fields_model_category(self):
        self.assertTrue(self.category.status)
        self.assertFalse(self.category.is_active)
        self.assertEquals(self.category.description, 'description fake')
        self.assertIsNotNone(self.category.parent_category)
        self.assertIsNotNone(self.category.created_at)

    def test_fields_model_sub_category(self):
        self.assertTrue(self.sub_category.status)
        self.assertFalse(self.sub_category.is_active)
        self.assertEquals(self.sub_category.description, 'sub description fake')
        self.assertIsNotNone(self.sub_category.created_at)
