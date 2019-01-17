from django.db import models

# Create your models here.
class CourseManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData['name']) < 5:
            errors['name'] = "Name must be at least 5 characters"
        if len(postData['description']) < 15:
            errors['description'] = "Description must be at least 15 characters"
        return errors

class Course(models.Model):
    name = models.CharField(max_length=80)
    objects = CourseManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Description(models.Model):
    text = models.TextField()
    course = models.OneToOneField(Course, related_name="description")
    