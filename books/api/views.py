from rest_framework.response import Response

from rest_framework.views import APIView

from books.models import Book
from books.choices import PERIOD_CHOICES

import random


def generate_quiz(books, question_type, answer_type):
	question_type_str = str(question_type)
	answer_type_str = str(answer_type)
	answer_type_str_query = answer_type_str + "__in"
	questions = []
	questions_ids = []

	excluded_books_for_questions = books
	c = 0

	while c < 10:
		excluded_books_for_questions.exclude(id__in=questions_ids)
		question = random.choice(excluded_books_for_questions)
		questions_ids.append(question.id)

		correct_answer = str(getattr(question, answer_type_str))

		answers_for_a_question = [correct_answer]

		excluded_books_for_answers = books
		while len(answers_for_a_question) < 5:
			excluded_books_for_answers = excluded_books_for_answers.exclude(**{answer_type_str_query: answers_for_a_question})

			answer = random.choice(excluded_books_for_answers)

			answers_for_a_question.append(getattr(answer, answer_type_str))

		random.shuffle(answers_for_a_question)

		questions.append(dict(soru=getattr(question, question_type_str), dogruCevap=correct_answer,
		                      cevaplar=answers_for_a_question))
		c = c + 1

	return questions


class QuizWithPeriodListAPIView(APIView):

	period_list = PERIOD_CHOICES

	def get(self, request, *args, **kwargs):
		question_type = self.kwargs.get("question")
		answer_type = self.kwargs.get("answer")
		period = int(self.kwargs.get("period"))

		period_alias = self.period_list[period]
		title = question_type.title() + " - " + answer_type.title() + ": " + period_alias
		books = Book.objects.all().filter(donem=period_alias)

		questions = generate_quiz(books, question_type, answer_type)

		return Response(dict(title=title, quiz=questions))


class QuizWithoutPeriodListAPIView(APIView):

	def get(self, request, *args, **kwargs):
		question_type = self.kwargs.get("question")
		answer_type = self.kwargs.get("answer")

		books = Book.objects.all()

		questions = generate_quiz(books, question_type, answer_type)

		return Response({'quiz': questions})
