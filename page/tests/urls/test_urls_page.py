from django.test import SimpleTestCase
from django.urls import resolve, reverse

from page.api.viewset import PageViewSet


class UrlPageTestCase(SimpleTestCase):
    def test_app_name(self):
        self.assertEquals(resolve("/en/api/v1/page/").app_name, "page")
        self.assertIsNotNone(resolve("/en/api/v1/page/").app_name)

    def test_url_page_list_create(self):
        path = reverse('page:page-list')
        self.assertEquals(resolve(path).func.__name__, PageViewSet.__name__)

    def test_url_page_detail_update_delete(self):
        path = reverse('page:page-detail', kwargs={'pk': 1})
        self.assertEquals(resolve(path).func.__name__, PageViewSet.__name__)
