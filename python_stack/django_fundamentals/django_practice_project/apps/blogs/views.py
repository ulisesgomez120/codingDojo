from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("placeholder to later display all the list of blogs")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    return redirect(index)

def show(request, num):
    return HttpResponse(f"placeholder to display blog {num}")

def edit(request, num):
    return HttpResponse(f"placeholder to edit blog {num}")

def destroy(request, num):
    return redirect(index)