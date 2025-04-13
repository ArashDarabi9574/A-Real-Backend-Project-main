from django.test import SimpleTestCase
from django.urls import reverse, resolve
from blog.api.viewset import CategoryViewSet, PostViewSet


class CategoryUrlTestCase(SimpleTestCase):
    def test_app_name(self):
        self.assertEquals(
            resolve('/en/api/v1/blog/category/').app_name, 'blog')

    def test_category_list_create_router(self):
        path = reverse('blog:category-list')
        self.assertEquals(resolve(path).func.__name__,
                          CategoryViewSet.__name__)
        self.assertNotEquals(resolve(path).func.__name__, PostViewSet.__name__)

    def test_category_detail_update_delete_router(self):
        path = reverse('blog:category-detail', kwargs={'pk': 1})
        self.assertEquals(resolve(path).func.__name__,
                          CategoryViewSet.__name__)
        self.assertNotEquals(resolve(path).func.__name__, PostViewSet.__name__)
