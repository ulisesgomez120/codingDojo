from django.db import models
from ..users.models import User
import re
# Create your models here.
class MessageManager(models.Manager):
    def validate_message(self, data):
        error = ''
        if len(data['message']) < 3:
            error = 'Message must be at least 3 characters'
        if len(data['message']) > 240:
            error = 'Message must be less than 240 characters'
        return error

    def validate_comment(self, data):
        error = ''
        if len(data['comment']) < 3:
            error = 'Comment must be at least 3 characters'
        if len(data['comment']) > 240:
            error = 'Comment must be less than 240 characters'
        return error

    def create_message(self, data, user_id):
        user_list = User.objects.filter(id=user_id)
        user = user_list[0]
        Message.objects.create(text=data['message'], creator=user)
        
    def create_comment(self, data, user_id):
        cleaned = {
            "message_id": data['message_id'],
        }
        user_list = User.objects.filter(id=user_id)
        message_list = Message.objects.filter(id=cleaned["message_id"])
        user = user_list[0]
        message = message_list[0]
        Comment.objects.create(text=data['comment'], creator=user, message=message)
        

class Message(models.Model):
    text = models.TextField()
    creator = models.ForeignKey(User, related_name="messages")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = MessageManager()

class Comment(models.Model):
    text = models.TextField()
    creator = models.ForeignKey(User, related_name="comments")
    message = models.ForeignKey(Message, related_name="comments")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = MessageManager()