from django.db import models
from ..users.models import User
# Create your models here.
class BookManager(models.Manager):
    def validate_book(self, data):
        errors = []
        if len(data['title']) < 2:
            errors.append('Title must be at least 2 characters long')
        if len(data['review']) < 2 or len(data['review']) > 240:
            errors.append("Review must be more than 2 and less than 240 characters")
        return errors
    def create_book(self, data, loggedin_user):
        if len(data['new_author']) == 0:
            author = Author.objects.get(name=data['exsiting_author'])
        else:
            author = Author.objects.create(name=data['new_author'])
        book = Book.objects.create(name=data['title'], author=author)
        user_list = User.objects.filter(id=loggedin_user)
        user = user_list[0]
        Review.objects.create(content=data['review'], rating=data['rating'], book=book, reviewer=user)
        return book.id
    def validate_review(self, data):
        error = ''
        if len(data['review']) < 2 or len(data['review']) > 240:
            error = "Review must be more than 2 and less than 240 characters"
        return error

    def add_review(self, data, book_id, loggedin_user):
        book = Book.objects.get(id=book_id)
        user_list = User.objects.filter(id=loggedin_user)
        user = user_list[0]
        Review.objects.create(content=data['review'], rating=data['rating'], book=book, reviewer=user)




class Author(models.Model):
    name = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()

class Book(models.Model):
    name = models.CharField(max_length=80)
    author = models.ForeignKey(Author, related_name="books") # technically it can have more than one author but for simplicity's sake
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()

class Review(models.Model):
    content = models.TextField()
    rating = models.PositiveSmallIntegerField()
    book = models.ForeignKey(Book, related_name="reviews")
    reviewer = models.ForeignKey(User, related_name="reviews")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()
