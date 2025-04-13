import base64
import json
import tempfile

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model

from blog.models import PostComment, Post, PostCategory
from blog.api.serializers import (
    CreateUpdateCommentSerializer, DetailCommentSerializer, ListCommentSerializer
)


class CommentViewSetTestCase(APITestCase):
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
            thumbnail=tempfile.NamedTemporaryFile(suffix='.jpg').name
        )

        self.replay = PostComment.objects.create(
            name='replay admin',
            email='admin@gmail.com',
            message='reply admin admin',
            post=self.post,

            rate=2

        )

        self.comment = PostComment.objects.create(
            name='admin',
            email='admin@gmail.com',
            message='admin admin admin',
            post=self.post,
            reply=self.replay,

            rate=2

        )

        self.valid_data = {
            "name": 'valid name',
            "email": 'valid@gmail.com',
            "message": 'valid message',
            "post": self.post.id,

            "rate": 4
        }

        self.no_valid_data = {
            "name": '',
            "email": '',
            "message": '',
            "post": ''
        }

        self.update_valid_date = {
            "name": 'valid update name',
            "email": 'valid@gmail.com',
            "message": 'valid update message',
            "post": self.post.id,

            "rate": 5
        }

        self.no_update_valid_date = {
            "name": '',
            "email": '',
            "message": '',
            "post": ''
        }

    # -------------------------- List -------------------------------------
    def test_comment_list(self):
        path = reverse('blog:comment-list')
        response = self.client.get(path)

        categories = PostComment.objects.all()
        serializer = ListCommentSerializer(categories, many=True)

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.data['results'], serializer.data)

    # -------------------------- Create -------------------------------------
    def test_comment_create_valid_data(self):
        path = reverse('blog:comment-list')
        response = self.client.post(
            path=path, data=self.valid_data, **self.auth_headers)
        content = json.loads(response.content)

        serializer = CreateUpdateCommentSerializer(data=self.valid_data)
        serializer.is_valid(raise_exception=True)

        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(content.get('name'), self.valid_data.get('name'))
        self.assertEquals(content.get('email'), self.valid_data.get('email'))
        self.assertEquals(content.get('message'),
                          self.valid_data.get('message'))
        self.assertTrue(content.get('post'))
        self.assertTrue(content.get('status'))

        self.assertTrue(content.get('rate'), self.valid_data.get('rate'))

    def test_comment_create_no_valid_data(self):
        path = reverse('blog:comment-list')
        response = self.client.post(
            path=path, data=self.no_valid_data, **self.auth_headers)

        serializer = CreateUpdateCommentSerializer(data=self.no_valid_data)
        serializer.is_valid(raise_exception=False)

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotEquals(response.status_code, status.HTTP_201_CREATED)

    def test_comment_create_no_permission(self):
        path = reverse('blog:comment-list')
        response = self.client.post(path=path, data=self.no_valid_data)

        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertNotEquals(response.status_code, status.HTTP_201_CREATED)

        # -------------------------- Detail -------------------------------------

    def test_comment_detail(self):
        path = reverse('blog:comment-detail', kwargs={'pk': 1})
        response = self.client.get(path)

        category = PostComment.objects.get(id=self.category.id)
        serializer = DetailCommentSerializer(category)

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.data, serializer.data)

    # ---------------------------- Update ________________________________________
    def test_comment_update_valid_data(self):
        path = reverse('blog:comment-detail', kwargs={'pk': 1})
        response = self.client.put(
            path=path, data=self.update_valid_date, **self.auth_headers)
        content = json.loads(response.content)

        serializer = CreateUpdateCommentSerializer(data=self.update_valid_date)
        serializer.is_valid(raise_exception=True)

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(content.get('title'),
                          self.update_valid_date.get('title'))
        self.assertEquals(content.get('sub_category'),
                          self.update_valid_date.get('sub_category'))
        self.assertEquals(content.get('description'),
                          self.update_valid_date.get('description'))

        self.assertEquals(content.get('rate'),
                          self.update_valid_date.get('rate'))
        self.assertTrue(content.get('status'))

    def test_comment_update_no_valid_data(self):
        path = reverse('blog:comment-detail', kwargs={'pk': 1})
        response = self.client.put(
            path=path, data=self.no_update_valid_date, **self.auth_headers)

        serializer = CreateUpdateCommentSerializer(
            data=self.no_update_valid_date)
        serializer.is_valid(raise_exception=False)

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_comment_update_no_permission(self):
        path = reverse('blog:comment-detail', kwargs={'pk': 1})
        response = self.client.put(path=path, data=self.update_valid_date)

        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # -------------------------------- Pagination --------------------------
    def test_pagination_successes(self):
        path = reverse('blog:comment-list')
        response = self.client.get(path)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('next', response.data)
        self.assertIn('previous', response.data)
        self.assertEqual(len(response.data['results']), 2)
        self.assertEqual(response.data['count'], 2)

    def test_pagination_404(self):
        path = reverse('blog:comment-list')
        response = self.client.get(path + '?page=2')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertNotIn('next', response.data)
        self.assertNotIn('previous', response.data)
