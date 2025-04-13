import json
import base64

from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.test import APITestCase

from forms.models import ContactUs
from forms.api.serializer import (
    ListContactUsSerializer,
    DetailContactUsSerializer,
    CreateUpdateContactUsSerializer
)


class ContactUsViewSetTestCase(APITestCase):
    def setUp(self) -> None:
        self.obj = ContactUs.objects.create(
            name='admin',
            email='admin@gmail.com',
            phone_number='09390000000',
            message='Testing Model Contact US'
        )

        self.user = get_user_model().objects.create(
            username='user',
            email='user@gmail.com',
            is_staff=True,
        )
        self.user.set_password('user123123')
        self.user.save()

        self.auth_headers = {
            'HTTP_AUTHORIZATION': 'Basic ' + base64.b64encode('user:user123123'.encode()).decode()
        }

        self.valid_data = {
            'name': 'admin_two',
            'email': 'admintwo@gmail.com',
            'phone_number': '09390000001',
            'message': 'Testing Model Contact US Two'
        }

        self.no_valid_data = {
            'name': 'admin_two',
            'email': 'admintwo.com',
            'phone_number': '093900000001',
            'message': ''
        }

        self.valid_data_update = {
            'name': 'admin_update',
            'email': 'adminupdate@gmail.com',
            'phone_number': '09390000002',
            'message': 'Testing Model Contact US Update',
            'thumbnail': 'test.jpg',
        }

        self.no_valid_data_update = {
            'name': 'admin_two',
            'email': 'admintwo.com',
            'phone_number': '093900000001',
            'message': ''
        }

    # _________________________ List ______________________________
    def test_contact_us_list(self):
        path = reverse("forms:contact_us-list")

        response = self.client.get(path, **self.auth_headers)
        contact_us = ContactUs.objects.all()
        serializer = ListContactUsSerializer(contact_us, many=True)

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.data['results'], serializer.data)

    def test_contact_us_permission_list(self):
        path = reverse("forms:contact_us-list")
        response = self.client.get(path)

        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # _________________________ Create ______________________________
    def test_contact_us_create_valid_data(self):
        # http://127.0.0.1:8000/fa/api/v1/contact-us/
        path = reverse("forms:contact_us-list")

        serializer = CreateUpdateContactUsSerializer(data=self.valid_data)
        serializer.is_valid(raise_exception=True)

        response = self.client.post(path=path, data=serializer.data)
        # convert json bytes type=> dict type
        content = json.loads(response.content)

        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(content.get('name'), self.valid_data.get('name'))
        self.assertIsNotNone(content.get('email'))
        self.assertTrue(content.get('phone_number'))
        self.assertIsNotNone(content.get('message'))

    def test_contact_us_create_no_valid_data(self):
        # http://127.0.0.1:8000/fa/api/v1/contact-us/
        path = reverse("forms:contact_us-list")

        serializer = CreateUpdateContactUsSerializer(data=self.no_valid_data)
        serializer.is_valid(raise_exception=False)

        response = self.client.post(path=path, data=serializer.data)

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotEqual(response.status_code, status.HTTP_201_CREATED)

    # ________________________ Update ______________________________

    # def test_contact_us_update_valid_data(self):
    #     path = reverse("forms:contact_us-detail", kwargs={'pk': 1})  # http://127.0.0.1:8000/fa/api/v1/contact-us/1
    #
    #     serializer = CreateUpdateContactUsSerializer(data=self.valid_data_update)
    #     serializer.is_valid(raise_exception=True)
    #
    #     response = self.client.put(path=path, data=serializer.data)
    #     content = json.loads(response.content)  # convert json bytes type=> dict type
    #
    #     self.assertEquals(response.status_code, status.HTTP_200_OK)
    #     self.assertEquals(content.get('name'), self.valid_data_update.get('name'))
    #     self.assertNotEqual(content.get('phone_number'), self.valid_data.get('phone_number'))
    #     self.assertEqual(content.get('email'), self.valid_data_update.get('email'))
    #     self.assertIsNotNone(content.get('message'))

    def test_contact_us_update_no_valid_data(self):
        # http://127.0.0.1:8000/fa/api/v1/contact-us/1
        path = reverse("forms:contact_us-detail", kwargs={'pk': 1})

        serializer = CreateUpdateContactUsSerializer(
            data=self.no_valid_data_update)
        serializer.is_valid(raise_exception=False)

        response = self.client.put(path=path, data=serializer.data)

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotEqual(response.status_code, status.HTTP_201_CREATED)

    # ______________________ Detail ________________________________
    def test_contact_us_exist_detail(self):
        # http://127.0.0.1:8000/fa/api/v1/contact-us/1
        path = reverse("forms:contact_us-detail", kwargs={'pk': 1})
        response = self.client.get(path, **self.auth_headers)
        contact_us = ContactUs.objects.get(id=self.obj.id)

        serializer = DetailContactUsSerializer(contact_us)

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.data, serializer.data)

    def test_contact_us_not_exist_detail(self):
        # http://127.0.0.1:8000/fa/api/v1/contact-us/1
        path = reverse("forms:contact_us-detail", kwargs={'pk': 2})
        response = self.client.get(path, **self.auth_headers)

        self.assertEquals(response.status_code, status.HTTP_404_NOT_FOUND)

    # _____________________ Delete _________________________________
    def test_contact_us_delete(self):
        # http://127.0.0.1:8000/fa/api/v1/contact-us/1
        path = reverse("forms:contact_us-detail", kwargs={'pk': 1})
        response = self.client.delete(path, **self.auth_headers)
        contact_us = ContactUs.objects.all().count()

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEquals(contact_us, 0)

    # ------------------------------ Search ------------------------------------

    def test_contact_us_list_search_successes(self):
        path = reverse("forms:contact_us-list") + "?search=admin"
        response = self.client.get(path, **self.auth_headers)
        content = json.loads(response.content)

        self.assertEquals(len(content['results']), 1)

    def test_contact_us_list_search_no_successes(self):
        path = reverse("forms:contact_us-list") + "?search=xoxoxoxo"
        response = self.client.get(path, **self.auth_headers)
        content = json.loads(response.content)

        self.assertNotEquals(len(content['results']), 1)
        self.assertEquals(len(content['results']), 0)

    # ------------------------------ Filtering ------------------------------------

    def test_contact_us_filtering_successes(self):
        path = reverse("forms:contact_us-list") + "?name=admin"
        response = self.client.get(path, **self.auth_headers)
        content = json.loads(response.content)

        self.assertEquals(len(content['results']), 1)

    def test_contact_us_filtering_no_successes(self):
        path = reverse("forms:contact_us-list") + "?name=ssss"
        response = self.client.get(path, **self.auth_headers)
        content = json.loads(response.content)

        self.assertNotEquals(len(content['results']), 1)
        self.assertEquals(len(content['results']), 0)

    # -------------------------------- Pagination --------------------------
    def test_pagination_successes(self):
        path = reverse("forms:contact_us-list")
        response = self.client.get(path, **self.auth_headers)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('next', response.data)
        self.assertIn('previous', response.data)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['count'], 1)

    def test_pagination_404(self):
        path = reverse("forms:contact_us-list")
        response = self.client.get(path + '?page=2', **self.auth_headers)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertNotIn('next', response.data)
        self.assertNotIn('previous', response.data)
