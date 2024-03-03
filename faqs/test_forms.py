from django.test import TestCase
from .forms import QuestionForm


class TestQuestionForm(TestCase):

    def test_question_is_required(self):
        form = QuestionForm({'question': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('question', form.errors.keys())

    def test_answer_is_required(self):
        form = QuestionForm({'answer': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('answer', form.errors.keys())
