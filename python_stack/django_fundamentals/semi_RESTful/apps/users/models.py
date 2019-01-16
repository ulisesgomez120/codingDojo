from django.db import models
import re
# Create your models here.
class UserManager(models.Manager):
    def validator(self, postData):
        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        errors = {}
        if len(postData['first_name']) < 2:
            errors['first_name'] = "Name should be at least 2 characters long"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Name should be at least 2 characters long"
        if not email_regex.match(postData['email']):
            errors['email'] = "Not a valid email"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
