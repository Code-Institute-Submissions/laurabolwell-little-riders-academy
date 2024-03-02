from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Question


class TestFaqViews(TestCase):

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

    def test_view_faqs(self):
        url = reverse('faqs')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'faqs/faqs.html')
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'includes/navbar.html')
        self.assertTemplateUsed(response, 'includes/footer.html')

    def test_cannot_add_question_if_not_superuser(self):
        self.client.login(username='testuser', password='testpass')
        url = reverse('add_question')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('faqs'))

    def test_cannot_edit_question_if_not_superuser(self):
        self.client.login(username='testuser', password='testpass')
        question = Question.objects.create(
            question='Test Question', answer='Test Answer'
        )
        url = reverse('edit_question', args=[question.id])
        response = self.client.get(url)
        self.assertRedirects(response, reverse('faqs'))

    def test_get_add_question_page(self):
        self.client.login(username='admin', password='adminpass')
        url = reverse('add_question')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'faqs/add_question.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_get_edit_question_page(self):
        self.client.login(username='admin', password='adminpass')
        question = Question.objects.create(
            question='Test Question', answer='Test Answer'
        )
        url = reverse('edit_question', args=[question.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'faqs/edit_question.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_can_add_question(self):
        self.client.login(username='admin', password='adminpass')
        response = self.client.post(reverse('add_question'), {
            'question': 'Test added question',
            'answer': 'Test added answer'
        })
        self.assertRedirects(response, reverse('faqs'))

    def test_cannot_add_empty_question(self):
        self.client.login(username='admin', password='adminpass')
        initial_question_count = Question.objects.count()
        response = self.client.post(reverse('add_question'), {'question': ''})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Question.objects.count(), initial_question_count)

    def test_can_edit_question(self):
        self.client.login(username='admin', password='adminpass')
        question = Question.objects.create(
            question='Test Question', answer='Test Answer'
        )
        response = self.client.post(reverse(
            'edit_question', args=[question.id]), {
                'question': 'Test question updated',
                'answer': 'Test answer updates'
            })
        self.assertRedirects(response, reverse('faqs'))
        updated_question = Question.objects.get(id=question.id)
        self.assertFalse(question.question == updated_question.question)
        self.assertFalse(question.answer == updated_question.answer)

    def test_cannot_edit_question_or_answer_to_empty(self):
        self.client.login(username='admin', password='adminpass')
        question = Question.objects.create(
            question='Test Question', answer='Test Answer'
        )
        response = self.client.post(reverse(
            'edit_question', args=[question.id]),
            {'question': 'Test question updated'})
        self.assertEqual(response.status_code, 200)
        updated_question = Question.objects.get(id=question.id)
        self.assertTrue(question.question == updated_question.question)
        self.assertTrue(question.answer == updated_question.answer)

    def test_can_delete_question(self):
        self.client.login(username='admin', password='adminpass')
        question = Question.objects.create(
            question='Test Question', answer='Test Answer'
        )
        url = reverse('delete_question', args=[question.id])
        response = self.client.post(url)
        self.assertRedirects(response, reverse('faqs'))
        existing_items = Question.objects.filter(id=question.id)
        self.assertEqual(len(existing_items), 0)
