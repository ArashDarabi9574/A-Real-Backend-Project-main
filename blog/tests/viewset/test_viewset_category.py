import base64
import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model

from blog.models import PostCategory
from blog.api.serializers import (
    ListCategorySerializer, DetailCategorySerializer, CreateUpdateCategorySerializer
)


class CategoryViewSetTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create(
            username='user',
            is_staff=True,
        )
        self.user.set_password('user123123')
        self.user.save()

        self.auth_headers = {
            'HTTP_AUTHORIZATION': 'Basic ' + base64.b64encode('user:user123123'.encode()).decode()
        }

        self.sub_category = PostCategory.objects.create(
            title='sub category fake',
            description='sub description fake',
        )

        self.category = PostCategory.objects.create(
            title='category fake',
            description='description fake',
            parent_category=self.sub_category
        )

        self.valid_data = {
            "title": 'valid title',
            "description": 'description valid',
            "parent_category": self.sub_category.id
        }

        self.no_valid_data = {
            "title": '',
            "description": self.category,
            "parent_category": self.user
        }

        self.update_valid_date = {
            'title': 'title update valid',
            'description': 'description update valid',
            'categories': [self.category.id]
        }

        self.no_update_valid_date = {
            'title': '',
            'description': '',
            'categories': [self.user.id]
        }

    # -------------------------- List -------------------------------------
    def test_category_list(self):
        path = reverse('blog:category-list')
        response = self.client.get(path)

        categories = PostCategory.objects.all()
        serializer = ListCategorySerializer(categories, many=True)

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.data['results'], serializer.data)

    # -------------------------- Create -------------------------------------
    def test_category_create_valid_data(self):
        path = reverse('blog:category-list')
        response = self.client.post(
            path=path, data=self.valid_data, **self.auth_headers)
        content = json.loads(response.content)

        serializer = CreateUpdateCategorySerializer(data=self.valid_data)
        serializer.is_valid(raise_exception=True)

        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(content.get('title'), self.valid_data.get('title'))
        self.assertEquals(content.get('description'),
                          self.valid_data.get('description'))
        self.assertEquals(content.get('parent_category'),
                          self.valid_data.get('parent_category'))

    def test_category_create_no_valid_data(self):
        path = reverse('blog:category-list')
        response = self.client.post(
            path=path, data=self.no_valid_data, **self.auth_headers)

        serializer = CreateUpdateCategorySerializer(data=self.no_valid_data)
        serializer.is_valid(raise_exception=False)

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotEquals(response.status_code, status.HTTP_201_CREATED)

    def test_category_create_no_permission(self):
        path = reverse('blog:category-list')
        response = self.client.post(path=path, data=self.no_valid_data)
        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertNotEquals(response.status_code, status.HTTP_201_CREATED)

    # -------------------------- Detail -------------------------------------
    def test_category_detail(self):
        path = reverse('blog:category-detail', kwargs={'pk': 2})
        response = self.client.get(path)

        category = PostCategory.objects.get(id=self.category.id)
        serializer = DetailCategorySerializer(category)

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.data, serializer.data)

    # ---------------------------- Delete ________________________________________
    def test_category_delete(self):
        path = reverse('blog:category-detail', kwargs={'pk': 1})
        response = self.client.delete(path, **self.auth_headers)

        category = PostCategory.objects.all().count()

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEquals(category, 0)

    def test_category_delete_no_permission(self):
        path = reverse('blog:category-detail', kwargs={'pk': 1})
        response = self.client.delete(path)

        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # ---------------------------- Update ________________________________________
    def test_category_update_valid_data(self):
        path = reverse('blog:category-detail', kwargs={'pk': 1})
        response = self.client.put(
            path=path, data=self.update_valid_date, **self.auth_headers)
        content = json.loads(response.content)

        serializer = CreateUpdateCategorySerializer(
            data=self.update_valid_date)
        serializer.is_valid(raise_exception=True)

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(content.get('title'),
                          self.update_valid_date.get('title'))
        self.assertEquals(content.get('sub_category'),
                          self.update_valid_date.get('sub_category'))
        self.assertEquals(content.get('description'),
                          self.update_valid_date.get('description'))
        self.assertTrue(content.get('status'))

    def test_category_update_no_valid_data(self):
        path = reverse('blog:category-detail', kwargs={'pk': 1})
        response = self.client.put(
            path=path, data=self.no_update_valid_date, **self.auth_headers)

        serializer = CreateUpdateCategorySerializer(
            data=self.no_update_valid_date)
        serializer.is_valid(raise_exception=False)

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_category_update_no_permission(self):
        path = reverse('blog:category-detail', kwargs={'pk': 1})
        response = self.client.put(path=path, data=self.update_valid_date)

        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)

# ------------------------------ Search ------------------------------------

    def test_category_list_search_successes(self):
        path = reverse("blog:category-list") + "?search=category+fake"
        response = self.client.get(path, **self.auth_headers)
        content = json.loads(response.content)

        self.assertEquals(len(content['results']), 2)

    def test_category_list_search_no_successes(self):
        path = reverse("blog:category-list") + "?search=xoxoxoxo"
        response = self.client.get(path, **self.auth_headers)
        content = json.loads(response.content)

        self.assertNotEquals(len(content['results']), 1)
        self.assertEquals(len(content['results']), 0)

        # ------------------------------ Filtering ------------------------------------

    def test_category_list_filtering_successes(self):
        path = reverse("blog:category-list") + "?title=category+fake"
        response = self.client.get(path, **self.auth_headers)
        content = json.loads(response.content)

        self.assertEquals(len(content['results']), 1)

    def test_category_list_filtering_no_successes(self):
        path = reverse("blog:category-list") + "?title=xoxoxoxo"
        response = self.client.get(path, **self.auth_headers)
        content = json.loads(response.content)

        self.assertNotEquals(len(content['results']), 1)
        self.assertEquals(len(content['results']), 0)

    # -------------------------------- Pagination --------------------------
    def test_pagination_successes(self):
        path = reverse("blog:category-list")
        response = self.client.get(path)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('next', response.data)
        self.assertIn('previous', response.data)
        self.assertEqual(len(response.data['results']), 2)
        self.assertEqual(response.data['count'], 2)

    def test_pagination_404(self):
        path = reverse("blog:category-list")
        response = self.client.get(path + '?page=2')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertNotIn('next', response.data)
        self.assertNotIn('previous', response.data)
