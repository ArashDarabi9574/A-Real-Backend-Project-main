import json
import base64

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model

from blog.models import Post, PostCategory
from blog.api.serializers import (
    ListPostSerializer, DetailPostSerializer, CreateUpdatePostSerializer
)


class PostViewSetTestCase(APITestCase):
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
        self.category = PostCategory.objects.create(
            title='category fake',
            description='description fake',
        )

        self.post = Post.objects.create(
            title='post fake',
            content='content fake',
            author=self.user,
            category=self.category,
        )

        self.valid_data = {
            "title": 'valid title',
            "content": 'description valid',
            'category': self.category.id

        }

        self.no_valid_data = {
            "title": '',
            "description": self.category,
            "parent_category": self.user
        }

        self.update_valid_date = {
            "title": 'valid update title',
            "content": 'description update valid',
            'category': self.category.id
        }

        self.no_update_valid_date = {
            'title': '',
            'description': '',
            'categories': self.user.id
        }

    # -------------------------- List -------------------------------------
    def test_post_list(self):
        path = reverse('blog:post-list')
        response = self.client.get(path)

        categories = Post.objects.all()
        serializer = ListPostSerializer(categories, many=True)

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.data['results'], serializer.data)

    # -------------------------- Create -------------------------------------
    def test_post_create_valid_data(self):
        path = reverse('blog:post-list')
        response = self.client.post(
            path=path, data=self.valid_data, **self.auth_headers)
        content = json.loads(response.content)

        serializer = CreateUpdatePostSerializer(data=self.valid_data)
        serializer.is_valid(raise_exception=True)

        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(content.get('title'), self.valid_data.get('title'))
        self.assertEquals(content.get('content'),
                          self.valid_data.get('content'))
        self.assertTrue(content.get('slug'))
        self.assertTrue(content.get('category'))

    def test_post_create_no_valid_data(self):
        path = reverse('blog:post-list')
        response = self.client.post(
            path=path, data=self.no_valid_data, **self.auth_headers)

        serializer = CreateUpdatePostSerializer(data=self.no_valid_data)
        serializer.is_valid(raise_exception=False)

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotEquals(response.status_code, status.HTTP_201_CREATED)

    def test_post_create_no_permission(self):
        path = reverse('blog:post-list')
        response = self.client.post(path=path, data=self.no_valid_data)

        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertNotEquals(response.status_code, status.HTTP_201_CREATED)

    # -------------------------- Detail -------------------------------------
    def test_post_detail(self):
        path = reverse('blog:post-detail', kwargs={'pk': 1})
        response = self.client.get(path)

        category = Post.objects.get(id=self.category.id)
        serializer = DetailPostSerializer(category)

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.data, serializer.data)

    # ---------------------------- Delete ________________________________________
    def test_post_delete(self):
        path = reverse('blog:post-detail', kwargs={'pk': 1})
        response = self.client.delete(path, **self.auth_headers)

        category = Post.objects.all().count()

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEquals(category, 0)

    def test_post_delete_no_permission(self):
        path = reverse('blog:post-detail', kwargs={'pk': 1})
        response = self.client.delete(path)

        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # ---------------------------- Update ________________________________________
    def test_post_update_valid_data(self):
        path = reverse('blog:post-detail', kwargs={'pk': 1})
        response = self.client.put(
            path=path, data=self.update_valid_date, **self.auth_headers)
        content = json.loads(response.content)

        serializer = CreateUpdatePostSerializer(data=self.update_valid_date)
        serializer.is_valid(raise_exception=True)

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(content.get('title'),
                          self.update_valid_date.get('title'))
        self.assertEquals(content.get('content'),
                          self.update_valid_date.get('content'))
        self.assertTrue(content.get('slug'))
        self.assertTrue(content.get('category'))

    def test_post_update_no_valid_data(self):
        path = reverse('blog:post-detail', kwargs={'pk': 1})
        response = self.client.put(
            path=path, data=self.no_update_valid_date, **self.auth_headers)

        serializer = CreateUpdatePostSerializer(data=self.no_update_valid_date)
        serializer.is_valid(raise_exception=False)

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_update_no_permission(self):
        path = reverse('blog:post-detail', kwargs={'pk': 1})
        response = self.client.put(path=path, data=self.update_valid_date)

        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)

        # ------------------------------ Search ------------------------------------

    def test_post_list_search_successes(self):
        path = reverse('blog:post-list') + "?search=post+fake"
        response = self.client.get(path, **self.auth_headers)
        content = json.loads(response.content)

        self.assertEquals(len(content['results']), 1)

    def test_category_list_search_no_successes(self):
        path = reverse('blog:post-list') + "?search=xoxoxoxo"
        response = self.client.get(path, **self.auth_headers)
        content = json.loads(response.content)

        self.assertNotEquals(len(content['results']), 1)
        self.assertEquals(len(content['results']), 0)

        # ------------------------------ Filtering ------------------------------------

    def test_post_list_filtering_successes(self):
        path = reverse("blog:post-list") + "?title=post+fake"
        response = self.client.get(path, **self.auth_headers)
        content = json.loads(response.content)

        self.assertEquals(len(content['results']), 1)

    def test_post_list_filtering_no_successes(self):
        path = reverse("blog:post-list") + "?title=xoxoxoxo"
        response = self.client.get(path, **self.auth_headers)
        content = json.loads(response.content)

        self.assertNotEquals(len(content['results']), 1)
        self.assertEquals(len(content['results']), 0)

    # -------------------------------- Pagination --------------------------
    def test_pagination_successes(self):
        path = reverse('blog:post-list')
        response = self.client.get(path)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('next', response.data)
        self.assertIn('previous', response.data)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['count'], 1)

    def test_pagination_404(self):
        path = reverse('blog:post-list')
        response = self.client.get(path + '?page=2')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertNotIn('next', response.data)
        self.assertNotIn('previous', response.data)
