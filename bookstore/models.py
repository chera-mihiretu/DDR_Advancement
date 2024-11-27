from django.db import models
from typing import *
# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publication_date = models.DateField()
    pages = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    genre = models.CharField(max_length=200)
    likes = models.IntegerField(default=0)
    def __str__(self) -> str:
        return self.title


class BookComments(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    comment = models.TextField()
    def __str__(self) -> str:
        return self.comment

