from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Lesson


class TestLessonViews(TestCase):

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

    def test_can_get_lessons_page(self):
        url = reverse('lessons')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lessons/lessons.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_can_get_lesson_details_page(self):
        lesson = Lesson.objects.create(
            name='Test',
            description='Test',
            min_age=2,
            max_age=10,
            class_size=10,
            duration=60,
            price=5.50,
            day='Saturday',
            time='12:00pm',
            image='lessons/1.png'
        )
        url = reverse('lesson_details', args=[lesson.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lessons/lesson_details.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_cannot_add_lesson_if_not_superuser(self):
        self.client.login(username='testuser', password='testpass')
        url = reverse('add_lesson')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('lessons'))

    def test_cannot_edit_lesson_if_not_superuser(self):
        self.client.login(username='testuser', password='testpass')
        lesson = Lesson.objects.create(
            name='Test',
            description='Test',
            min_age=2,
            max_age=10,
            class_size=10,
            duration=60,
            price=5.50,
            day='Saturday',
            time='12:00pm',
            image='lessons/1.png'
        )
        url = reverse('edit_lesson', args=[lesson.id])
        response = self.client.get(url)
        self.assertRedirects(response, reverse('lessons'))

    def test_get_add_lesson_page(self):
        self.client.login(username='admin', password='adminpass')
        url = reverse('add_lesson')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lessons/add_lesson.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_get_edit_lesson_page(self):
        self.client.login(username='admin', password='adminpass')
        lesson = Lesson.objects.create(
            name='Test',
            description='Test',
            min_age=2,
            max_age=10,
            class_size=10,
            duration=60,
            price=5.50,
            day='Saturday',
            time='12:00pm',
            image='lessons/1.png'
        )
        url = reverse('edit_lesson', args=[lesson.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lessons/edit_lesson.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_can_delete_lesson(self):
        self.client.login(username='admin', password='adminpass')
        lesson = Lesson.objects.create(
            name='Test',
            description='Test',
            min_age=2,
            max_age=10,
            class_size=10,
            duration=60,
            price=5.50,
            day='Saturday',
            time='12:00pm',
            image='lessons/1.png'
        )
        url = reverse('delete_lesson', args=[lesson.id])
        response = self.client.post(url)
        self.assertRedirects(response, reverse('lessons'))
        existing_items = Lesson.objects.filter(id=lesson.id)
        self.assertEqual(len(existing_items), 0)
