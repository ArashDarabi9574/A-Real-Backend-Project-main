import base64
import json
import tempfile

from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from page.models import Page
from page.api.serializer import (
    PageListSerializer,
    PageDetailSerializer,
    PageCreateUpdateSerializer
)


class ViewSetPageTestCase(APITestCase):
    def setUp(self) -> None:
        self.author = get_user_model().objects.create(
            username='author',
            is_staff=True
        )
        self.author.set_password('author123123')
        self.author.save()

        self.auth_headers = {
            'HTTP_AUTHORIZATION': 'Basic ' + base64.b64encode('author:author123123'.encode()).decode()
        }

        self.obj = Page.objects.create(
            title='title fake',
            content='content fake',
            author=self.author,
            status='PU',
        )

        self.valid_data = {
            'title': 'title valid',
            'content': 'content valid',
            'author': self.author,
            'status': 'IN',
            'custom_template': True,
            'is_active': True,

        }

        self.no_valid_data = {
            'title': 22,
            'content': 'content valid',
            'author': 'autor no valid',
            'status': 'IN',
            'custom_template': True,
            'is_active': self.author,
        }

        self.valid_data_update = {
            'title': 'title update valid',
            'content': 'content update valid',
            'author': self.author,
            'status': 'IN',
            'custom_template': True,
            'is_active': True,
            'thumbnail': tempfile.NamedTemporaryFile(suffix='.jpg').name
        }

        self.no_valid_data_update = {
            'title': 22,
            'content': 'content valid',
            'author': '',
            'status': 'IN',
            'custom_template': True,
            'is_active': self.author,
        }

    # ________________________ List ______________________________
    def test_page_list(self):
        path = reverse('page:page-list')
        response = self.client.get(path, **self.auth_headers)

        page = Page.objects.all()
        serializer = PageListSerializer(page, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.data['results'], serializer.data)

    # ________________________ Create ______________________________
    def test_page_create_valid_data(self):
        path = reverse('page:page-list')
        response = self.client.post(path, self.valid_data, **self.auth_headers)

        serializer = PageCreateUpdateSerializer(data=self.valid_data)
        serializer.is_valid(raise_exception=True)
        content = json.loads(response.content)

        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(content.get('title'), self.valid_data.get('title'))
        self.assertTrue(content.get('slug'))
        self.assertTrue(content.get('status'))

    def test_page_create_no_valid_data(self):
        path = reverse('page:page-list')
        response = self.client.post(
            path, self.no_valid_data, **self.auth_headers)

        serializer = PageCreateUpdateSerializer(data=self.no_valid_data)
        serializer.is_valid(raise_exception=False)

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotEqual(response.status_code, status.HTTP_201_CREATED)

    # ________________________ Detail ______________________________
    def test_page_create_no_permission(self):
        path = reverse('page:page-list')
        response = self.client.post(path, self.valid_data)

        serializer = PageCreateUpdateSerializer(data=self.valid_data)
        serializer.is_valid(raise_exception=True)

        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertNotEqual(response.status_code, status.HTTP_201_CREATED)

    def test_page_detail(self):
        path = reverse('page:page-detail', kwargs={'pk': 1})
        response = self.client.get(path)

        page = Page.objects.get(id=self.obj.id)
        serializer = PageDetailSerializer(page)

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_page_not_exist_detail(self):
        path = reverse('page:page-detail', kwargs={'pk': 2})
        response = self.client.get(path)

        self.assertEquals(response.status_code, status.HTTP_404_NOT_FOUND)

    # ________________________ Delete ______________________________
    def test_page_delete(self):
        path = reverse('page:page-detail', kwargs={'pk': 1})
        response = self.client.delete(path, **self.auth_headers)
        page = Page.objects.all().count()

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEquals(page, 0)

    # ________________________ Update ______________________________

    # def test_page_update_valid_data(self):
    #     path = reverse("page:page-detail", kwargs={'pk': 1})  # http://127.0.0.1:8000/fa/api/v1/page/1
    #
    #     serializer = PageCreateUpdateSerializer(data=self.valid_data_update,files=self.valid_data_update)
    #     serializer.is_valid(raise_exception=True)
    #
    #     response = self.client.put(path=path, data=serializer.data,content_type='file', **self.auth_headers)
    #     content = json.loads(response.content)  # convert json bytes type=> dict type
    #
    #     self.assertEquals(response.status_code, status.HTTP_200_OK)
    #     self.assertEquals(content.get('title'), self.valid_data_update.get('title'))
    #     self.assertEqual(content.get('slug'), self.valid_data.get('slug'))
    #     self.assertEqual(content.get('email'), self.valid_data_update.get('email'))
    #     self.assertIsNotNone(content.get('status'))
    #     self.assertIsNotNone(content.get('custom_template'))

    def test_page_update_no_valid_data(self):
        # http://127.0.0.1:8000/fa/api/v1/page/1
        path = reverse("page:page-detail", kwargs={'pk': 1})

        serializer = PageCreateUpdateSerializer(data=self.no_valid_data_update)
        serializer.is_valid(raise_exception=False)

        response = self.client.put(
            path=path, data=serializer.data, **self.auth_headers)

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotEqual(response.status_code, status.HTTP_201_CREATED)

        # ------------------------------ Search ------------------------------------

    def test_page_list_search_successes(self):
        path = reverse('page:page-list') + "?search=title+fake"
        response = self.client.get(path, **self.auth_headers)
        content = json.loads(response.content)

        self.assertEquals(len(content['results']), 1)

    def test_page_list_search_no_successes(self):
        path = reverse('page:page-list') + "?search=sdsds"
        response = self.client.get(path, **self.auth_headers)
        content = json.loads(response.content)

        self.assertNotEquals(len(content['results']), 1)
        self.assertEquals(len(content['results']), 0)

        # ------------------------------ Filtering ------------------------------------

    def test_page_filtering_successes(self):
        path = reverse('page:page-list') + "?title=title+fake"
        response = self.client.get(path, **self.auth_headers)
        content = json.loads(response.content)

        self.assertEquals(len(content['results']), 1)

    def test_page_filtering_no_successes(self):
        path = reverse('page:page-list') + "?title=nima@gmail.com"
        response = self.client.get(path, **self.auth_headers)
        content = json.loads(response.content)

        self.assertNotEquals(len(content['results']), 1)
        self.assertEquals(len(content['results']), 0)

        # -------------------------------- Pagination --------------------------

    def test_pagination_successes(self):
        path = reverse('page:page-list')
        response = self.client.get(path, **self.auth_headers)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('next', response.data)
        self.assertIn('previous', response.data)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['count'], 1)

    def test_pagination_404(self):
        path = reverse('page:page-list')
        response = self.client.get(path + '?page=2', **self.auth_headers)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertNotIn('next', response.data)
        self.assertNotIn('previous', response.data)
