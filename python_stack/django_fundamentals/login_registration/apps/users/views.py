from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
# Create your views here.
def index(req):
    context = {
        'users': User.objects.all()
    }
    return render(req, "users/index.html", context)

def create(req):
    req.session.clear()
    if req.method == "POST":
        errors = User.objects.validate_register(req.POST)
        if errors:
            for error in errors:
                messages.error(req, error)
            return redirect('/')
        user = User.objects.create_user(req.POST)
        req.session["user_id"] = user.id
        return redirect('/users/success/')
    else:
        return redirect('/')

def login(req):
    if req.method == "POST":
        valid, response = User.objects.validate_login(req.POST)
        if not valid:
            messages.error(req, response)
            return redirect('/')
        req.session['user_id'] = response.id
        return redirect('/users/success/')

def logout(req):
    req.session.clear()

def success(req):
    if 'user_id' not in req.session:
        messages.error(req, "Not logged in")
        return redirect('/')
    return render(req, "users/success.html")
