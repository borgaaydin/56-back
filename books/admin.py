from django.contrib import admin
from .models import Book

# Register your models here.


class BookAdmin(admin.ModelAdmin):
	search_fields = ["eser", "donem", "yazar"]
	list_display = ["eser", "yazar", "donem", "akim", "tur"]


admin.site.register(Book, BookAdmin)
