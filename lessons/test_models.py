from django.test import TestCase
from .models import Lesson


class TestLessonModels(TestCase):

    def test_min_age_defaults_to_2(self):
        lesson = Lesson.objects.create(
            name='Test',
            description='Test',
        )
        self.assertEqual(lesson.min_age, 2)

    def test_max_age_defaults_to_10(self):
        lesson = Lesson.objects.create(
            name='Test',
            description='Test',
        )
        self.assertEqual(lesson.max_age, 10)

    def test_class_size_defaults_to_12(self):
        lesson = Lesson.objects.create(
            name='Test',
            description='Test',
        )
        self.assertEqual(lesson.class_size, 12)

    def test_duration_defaults_to_45(self):
        lesson = Lesson.objects.create(
            name='Test',
            description='Test',
        )
        self.assertEqual(lesson.duration, 45)

    def test_price_defaults_to_475(self):
        lesson = Lesson.objects.create(
            name='Test',
            description='Test',
        )
        self.assertEqual(lesson.price, 4.75)

    def test_day_age_defaults_to_saturday(self):
        lesson = Lesson.objects.create(
            name='Test',
            description='Test',
        )
        self.assertEqual(lesson.day, "Saturday")

    def test_time_defaults_to_12pm(self):
        lesson = Lesson.objects.create(
            name='Test',
            description='Test',
        )
        self.assertEqual(lesson.time, "12:00pm")
