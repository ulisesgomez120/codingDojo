from django.shortcuts import render,redirect
from django.contrib import messages

# Create your views here.
def index(req):
    if "user_id" not in req.session:
        messages.error(req, "You are not logged in")
        return redirect("user:index")
    return render(req, "books/index.html")

