from django.test import TestCase
from .forms import LessonForm


class TestLessonForm(TestCase):

    def test_name_is_required(self):
        form = LessonForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())

    def test_description_is_required(self):
        form = LessonForm({'description': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('description', form.errors.keys())

    def test_min_age_is_required(self):
        form = LessonForm({'min_age': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('min_age', form.errors.keys())

    def test_max_age_is_required(self):
        form = LessonForm({'max_age': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('max_age', form.errors.keys())

    def test_class_size_is_required(self):
        form = LessonForm({'class_size': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('class_size', form.errors.keys())

    def test_duration_is_required(self):
        form = LessonForm({'duration': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('duration', form.errors.keys())

    def test_price_is_required(self):
        form = LessonForm({'price': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('price', form.errors.keys())

    def test_day_is_required(self):
        form = LessonForm({'day': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('day', form.errors.keys())

    def test_time_is_required(self):
        form = LessonForm({'time': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('time', form.errors.keys())

    def test_image_is_required(self):
        form = LessonForm({'image': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('image', form.errors.keys())
