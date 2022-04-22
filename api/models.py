from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)


class BookDetails(models.Model):
    bok = models.ForeignKey('Book',on_delete=models.CASCADE,related_name='rbook')
    summary = models.CharField(max_length=300)
    