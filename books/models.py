from django.db import models

# Create your models here.

class Book(models.Model):
	akim = models.CharField(max_length= 100, null=True, blank=True)
	donem = models.CharField(max_length= 100)
	yazar = models.CharField(max_length= 200)
	eser = models.CharField(max_length= 200)
	tur = models.CharField(max_length= 100)

	def __str__(self):
		return str(self.eser)