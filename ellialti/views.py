from django.shortcuts import render, get_object_or_404

from django.views.generic import TemplateView

from books.models import Book

import random

class HomeView(TemplateView):
    template_name = 'home.html'
    

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        books = Book.objects.all()
        booksCount = Book.objects.count()
        questionType = "eser"
        answerType = "yazar"

        questions = []
        questionsIds = []

        excludedBooksForQuestions = books
        c = 0

        while c < 10:
            excludedBooksForQuestions.exclude(id__in=questionsIds)
            question = random.choice(excludedBooksForQuestions)
            questionsIds.append(question.id)

            answersForAQuestion = [question.yazar]
            answersIds = []
            
            excludedBooksForAnswers = books
            while len(answersForAQuestion) < 5:
                excludedBooksForAnswers = excludedBooksForAnswers.exclude(id__in=answersIds).exclude(yazar__in=answersForAQuestion)
                answer = random.choice(excludedBooksForAnswers)
                answersForAQuestion.append(answer.yazar)

            random.shuffle(answersForAQuestion)
            questions.append({'soru': question.eser, 'dogruCevap': question.yazar, 'cevaplar': answersForAQuestion})
            c = c + 1

        context['questions'] = questions
        return context

    