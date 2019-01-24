from django.shortcuts import render, redirect
from .models import Message, Comment
from django.contrib import messages

# Create your views here.
def dash(req):
    if 'user_id' not in req.session:
        messages.error(req, "Not logged in")
        return redirect('/')
    context = {
        "posts": Message.objects.order_by('created_at'),
        "comments": Comment.objects.order_by('created_at')
    }
    for comment in context['comments']:
        print(comment.message.id)
    return render(req, 'posts/wall.html', context)

def create_message(req):
    if req.method == "POST":
        error = Message.objects.validate_message(req.POST)
        print(error)
        if error != '':
            messages.error(req, error)
            return redirect('/wall')
        Message.objects.create_message(req.POST, req.session['user_id'])
        return redirect('/wall')   
    else:
        return redirect('/wall')

def create_comment(req):
    if req.method == "POST":
        error = Comment.objects.validate_comment(req.POST)
        if error != '':
            messages.error(req, error)
            return redirect('/wall')
        Comment.objects.create_comment(req.POST, req.session['user_id'])
    return redirect('/wall')
