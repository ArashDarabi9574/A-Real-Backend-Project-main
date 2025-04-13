from django.test import TestCase
from forms.models import ContactUs


class ContactUSModelTestCase(TestCase):
    def setUp(self) -> None:
        self.obj = ContactUs.objects.create(
            name='admin',
            email='admin@gmail.com',
            phone_number='09390000000',
            message='Testing Model Contact US'
        )

    def test_method_str(self):
        self.assertIsNotNone(str(self.obj))
        self.assertEqual(str(self.obj), 'admin')
        self.assertNotEqual(str(self.obj), 'admin@gmail.com')

    def test_fields_contact_us_model(self):
        self.assertEqual(self.obj.email, 'admin@gmail.com')
        self.assertNotEqual(self.obj.email, 'admin2@gmail.com')

        self.assertEqual(self.obj.phone_number, '09390000000')
        self.assertNotEqual(self.obj.phone_number, '09390000001')

    def test_not_none_fields_contact_us_model(self):
        self.assertIsNotNone(self.obj.name)
        self.assertIsNotNone(self.obj.email)
        self.assertIsNotNone(self.obj.phone_number)
        self.assertIsNotNone(self.obj.message)
