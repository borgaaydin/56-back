from django.conf.urls import url

from .views import QuizWithPeriodListAPIView, QuizWithoutPeriodListAPIView

urlpatterns = [
	url(r'^(?P<question>[\w.@+-]+)/(?P<answer>[\w.@+-]+)/$', QuizWithoutPeriodListAPIView.as_view(), name='quiz-without-period'),
	url(r'^(?P<question>[\w.@+-]+)/(?P<answer>[\w.@+-]+)/(?P<period>[1-9]\d*)/$', QuizWithPeriodListAPIView.as_view(), name='quiz-with-period')
]
