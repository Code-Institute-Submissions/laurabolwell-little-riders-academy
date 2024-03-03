from django.test import TestCase
from .forms import ContactForm


class TestContactForm(TestCase):

    def test_contact_name_is_required(self):
        form = ContactForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())

    def test_contact_email_is_required(self):
        form = ContactForm({'email': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())

    def test_query_is_required(self):
        form = ContactForm({'query': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('query', form.errors.keys())

    def test_contact_booking_number_is_not_required(self):
        form = ContactForm({
            'booking_number': '', 'name': 'Test',
            'email': 'Test@test.com', 'query': 'Test',
        })
        self.assertTrue(form.is_valid())

    def test_fields_are_excluded_from_form(self):
        form = ContactForm()
        self.assertEqual(form.Meta.exclude, ('user', 'contact_date'))
