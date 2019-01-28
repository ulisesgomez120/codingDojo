from django.shortcuts import render,redirect, reverse
from django.contrib import messages
from ..users.models import User
from .models import Book, Author

# Create your views here.
def index(req):
    if "user_id" not in req.session:
        messages.error(req, "You are not logged in")
        return redirect("user:index")
    context = {
        "user": User.objects.get(id=req.session['user_id']),
        "books": Book.objects.all(),
        "recent": Book.objects.order_by("-created_at")[:3],
    }
    return render(req, "books/index.html", context)

def new(req):
    context = {
        'authors': Author.objects.all(),
    }
    return render(req, "books/new_book.html", context)

def create_book(req):
    if req.method == "POST":
        errors = Book.objects.validate_book(req.POST)
        if errors:
            for error in errors:
                messages.error(req, error)
            return redirect("book:new")
        book_id = Book.objects.create_book(req.POST,req.session['user_id'])
    return redirect("book:show", book_id=book_id)

def show(req, book_id):
    context = {
        "book": Book.objects.get(id=book_id),
        "reviews": Book.objects.get(id=book_id).reviews.all(),
    }
    return render(req, "books/show.html", context)

def add_review(req, book_id):
    if req.method == "POST":
        error = Book.objects.validate_review(req.POST)
        print(book_id)
        if error != '':
            messages.error(req, error)
            return redirect("book:show", book_id)
        Book.objects.add_review(req.POST, book_id, req.session['user_id'])
        return redirect("book:show", book_id)