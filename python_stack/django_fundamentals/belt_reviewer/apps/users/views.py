from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages

# Create your views here.
def index(req):
    context = {
        "users": User.objects.order_by("email")
    }
    return render(req, "users/login.html", context)

def create(req):
    if req.method == 'POST':
        errors = User.objects.validate_register(req.POST)
        if errors:
            for error in errors:
                messages.error(req, error)
            return redirect("user:index")
        user = User.objects.create_user(req.POST)
        req.session['user_id'] = user.id
        return redirect("book:index")
    else:
        return redirect("user:index")

def login(req):
    if req.method == 'POST':
        valid, response = User.objects.validate_login(req.POST)
        if not valid:
            messages.error(req, response)
            return redirect("user:index")
        req.session['user_id'] = response.id
        return redirect("book:index")

def logout(req):
    req.session.clear()
    messages.error(req, "You have been successfully logged out")
    return redirect("user:index")


