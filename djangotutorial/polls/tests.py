from django.test import TestCase
from .models import Question


class QuestionModelTests(TestCase):
    def test_str_returns_question_text(self):
        question = Question(question_text="How are you?")
        self.assertEqual(str(question), "How are you?")
