from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=15)
    pageNumber = models.IntegerField(default=100)
    genre = models.CharField(max_length=8)
    publishDate = models.DateTimeField('date published')

class Car(models.Model):
    make = models.CharField(max_length=10)
    model = models.CharField(max_length=12)
    year = models.IntegerField(default=2009)