from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User


class TestContactViews(TestCase):

    def setUp(self):
        # Create a regular user (non-superuser) for testing
        self.user = User.objects.create_user(
            username='testuser', password='testpass'
        )
        # Create a superuser for testing
        self.superuser = User.objects.create_superuser(
            username='admin', email='admin@example.com', password='adminpass'
        )
        # Create a client
        self.client = Client()

    def test_can_get_contact_page(self):
        url = reverse('contact')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contact.html')
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'includes/navbar.html')
        self.assertTemplateUsed(response, 'includes/footer.html')

    def test_cannot_get_view_queries_if_not_superuser(self):
        self.client.login(username='testuser', password='testpass')
        url = reverse('view_queries')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('contact'))

    def test_can_view_queries(self):
        self.client.login(username='admin', password='adminpass')
        url = reverse('view_queries')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/view_queries.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_can_send_query(self):
        response = self.client.post(reverse('contact'), {
            'name': 'Test',
            'email': 'test@test.com',
            'query': 'Test Query'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('lessons'))
