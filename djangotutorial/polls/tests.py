from django.test import TestCase
from .models import Question


class QuestionModelTests(TestCase):
    def test_str_returns_question_text(self):
        question = Question(question_text="Hello?")
        self.assertEqual(str(question), "Hello?")
