from django.db import models
import re
import bcrypt

# Create your models here.
class UserManager(models.Manager):
    def validate_register(self, data):
        errors = []
        name_regex = re.compile(r'[0-9]')
        password_regex = re.compile(r'[A-Z0-9]+')
        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(data['first_name']) < 2:
            errors.append('First name must be at least 2 characters long')
        if len(data['last_name']) < 2:
            errors.append('Last name must be at least 2 characters long')
        if name_regex.search(data["first_name"]) or name_regex.search(data["last_name"]):
            errors.append("No numbers accepted in name fields")
# email
        if not email_regex.match(data['email']):
            errors.append('Must enter a valid email')
        user_list = self.filter(email=data['email'])
        if user_list:
            errors.append("Somebody already has that email")
# password
        if len(data['password']) < 8:
            errors.append("Password must be more than 8 characters")
        if not password_regex.search(data["password"]):
            errors.append("Password must have at least 1 uppercase letter and at least 1 number")
        if not data['password'] == data['confirm_password']:
            errors.append("Passwords don't match")
        return errors

    def create_user(self, data):
        pw_hash = bcrypt.hashpw(data['password'].encode(), bcrypt.gensalt(12))
        return self.create(
            first_name=data['first_name'],
            last_name=data['last_name'],
            email=data['email'],
            pw_hash=pw_hash
        )
        
    def validate_login(self, data):
        user_list = self.filter(email=data['login_email'])
        if not user_list:
            return (False, "Email or Password is invalid")
        user = user_list[0]
        if bcrypt.checkpw(data['login_password'].encode(), user.pw_hash.encode()):
            return (True, user)
        else:
            return (False, "Email or Password is invalid")

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=90)
    pw_hash = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()