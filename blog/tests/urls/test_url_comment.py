from django.test import SimpleTestCase
from django.urls import reverse, resolve
from blog.api.viewset import PostCommentViewSet, PostViewSet


class CommentUrlTestCase(SimpleTestCase):
    def test_app_name(self):
        self.assertEquals(resolve('/en/api/v1/blog/comment/').app_name, 'blog')

    def test_comment_list_create_router(self):
        path = reverse('blog:comment-list')
        self.assertNotEquals(resolve(path).func.__name__, PostViewSet.__name__)
        self.assertEquals(resolve(path).func.__name__, PostCommentViewSet.__name__)

    def test_comment_detail_update_delete_router(self):
        path = reverse('blog:comment-detail', kwargs={'pk': 1})
        self.assertNotEquals(resolve(path).func.__name__, PostViewSet.__name__)
        self.assertEquals(resolve(path).func.__name__, PostCommentViewSet.__name__)
