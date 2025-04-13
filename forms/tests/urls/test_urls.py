from django.test import SimpleTestCase
from django.urls import reverse, resolve

from forms.api import viewset


class ContactUsUrlTestCase(SimpleTestCase):
    def test_app_name(self):
        self.assertEquals(resolve("/en/api/v1/contact-us/").app_name, "forms")
        self.assertIsNotNone(resolve("/en/api/v1/contact-us/").app_name)

    def test_contact_us_list(self):
        path = reverse('forms:contact_us-list')
        self.assertEquals(resolve(path).func.__name__, viewset.ContactUsViewSet.__name__)

    def test_contact_us_detail(self):
        path = reverse('forms:contact_us-detail', kwargs={'pk': 1})
        self.assertEquals(resolve(path).func.__name__, viewset.ContactUsViewSet.__name__)

    def test_contact_us_create(self):
        path = reverse('forms:contact_us-list')
        self.assertEquals(resolve(path).func.__name__, viewset.ContactUsViewSet.__name__)

    def test_contact_us_update(self):
        path = reverse('forms:contact_us-detail', kwargs={'pk': 1})
        self.assertEquals(resolve(path).func.__name__, viewset.ContactUsViewSet.__name__)

    def test_contact_us_partial_update(self):
        path = reverse('forms:contact_us-detail', kwargs={'pk': 1})
        self.assertEquals(resolve(path).func.__name__, viewset.ContactUsViewSet.__name__)

    def test_contact_us_delete(self):
        path = reverse('forms:contact_us-detail', kwargs={'pk': 1})
        self.assertEquals(resolve(path).func.__name__, viewset.ContactUsViewSet.__name__)
