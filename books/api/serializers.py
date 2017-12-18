from rest_framework import serializers
from books.models import Book

class QuizSerializer(serializers.Serializer):
    soru = serializers.CharField(max_length=1000)
    dogruCevap = serializers.CharField(max_length=1000)
    cevaplar = serializers.CharField(max_length=9000)