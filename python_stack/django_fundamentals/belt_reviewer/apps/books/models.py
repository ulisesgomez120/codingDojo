from django.db import models
from ..users.models import User
# Create your models here.
class BookManager(models.Manager):
    pass

class Author(models.Model):
    name = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()

class Book(models.Model):
    name = models.CharField(max_length=80)
    rating = models.PositiveSmallIntegerField()
    author = models.ForeignKey(Author, related_name="books") # technically it can have more than one author but for simplicity's sake
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()

class Review(models.Model):
    content = models.TextField()
    book = models.ForeignKey(Book, related_name="reviews")
    reviewer = models.ForeignKey(User, related_name="reviews")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()
