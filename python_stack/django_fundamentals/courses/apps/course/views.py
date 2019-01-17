from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        "courses": Course.objects.all()
    }
    return render(request, "course/index.html",context)

def create(request):
    if request.method == "POST":
        errors = Course.objects.validator(request.POST)
        if errors:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        Course.objects.create(name=request.POST['name'])
        course = Course.objects.last()
        Description.objects.create(text=request.POST['description'],course=course)
    return redirect('/')

def destroy(request, course_id):
    context = {
        "course": Course.objects.get(id=course_id)
    }
    return render(request, "course/danger.html",context)
def delete(request, course_id):
    Course.objects.get(id=course_id).delete()
    return redirect('/')