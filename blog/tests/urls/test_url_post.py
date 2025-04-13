from django.test import SimpleTestCase
from django.urls import reverse, resolve
from blog.api.viewset import CategoryViewSet, PostViewSet


class PostUrlTestCase(SimpleTestCase):
    def test_app_name(self):
        self.assertEquals(resolve('/en/api/v1/blog/post/').app_name, 'blog')

    def test_post_list_create_router(self):
        path = reverse('blog:post-list')
        self.assertNotEquals(resolve(path).func.__name__,
                             CategoryViewSet.__name__)
        self.assertEquals(resolve(path).func.__name__, PostViewSet.__name__)

    def test_post_detail_update_delete_router(self):
        path = reverse('blog:post-detail', kwargs={'pk': 1})
        self.assertNotEquals(resolve(path).func.__name__,
                             CategoryViewSet.__name__)
        self.assertEquals(resolve(path).func.__name__, PostViewSet.__name__)
