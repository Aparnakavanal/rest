from django.db import models

# Create your models here.

class Book(models.Model):
    book_name=models.CharField(max_length=120,unique=True)
    author=models.CharField(max_length=120)
    pages=models.CharField(max_length=40)
    price=models.FloatField()

    def __str__(self):
        return self.book_name
