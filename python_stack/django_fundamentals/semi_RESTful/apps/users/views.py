from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

# Create your views here.
def index(request):
    context = {
        "users": User.objects.all()
    }
    return render(request, 'users/dash.html', context)

def new(request):
    return render(request, 'users/user_registration.html')

def create(request):
    if request.method == "POST":
        errors = User.objects.validator(request.POST)
        if errors:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/users/new')
        print(request.POST)
        User.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'],email=request.POST['email'])
        return redirect('/users')
    else:
        return redirect('/users/new')

def show(request, user_id):
    context = {
        "user": User.objects.get(id=int(user_id))
    }
    return render(request, 'users/show.html',context)

def edit(request, user_id):
    context = {
        "user": User.objects.get(id=int(user_id))
    }
    return render(request, 'users/edit_user.html', context)

def update(request, user_id):
    if request.method == "POST":
        errors = User.objects.validator(request.POST)
        if errors:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/users/edit')
    return redirect('/users/' + id)

def destroy(request, user_id):
    a = User.objects.get(id=user_id)
    a.delete()
    return redirect('/users')