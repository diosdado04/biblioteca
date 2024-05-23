from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=255)

class Book(models.Model):
    title = models.CharField(max_length=255)
    editorial = models.TextField()
    best_seller = models.BooleanField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    author = models.ManyToManyField(Author)

class Stock(models.Model):
    name = models.CharField(max_length=255)
    book =  models.ForeignKey(Book, on_delete=models.CASCADE)
    sold = models.BooleanField()