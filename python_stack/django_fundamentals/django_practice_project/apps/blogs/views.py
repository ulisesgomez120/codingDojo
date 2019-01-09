from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("placeholder to later display all the list of blogs")

def new(request):
    return render(request, 'blogs/index.html')

def create(request):
    if request.method == "POST":
        print("*"*50)
        print(request.POST)
        print(request.POST['name'])
        print(request.POST['desc'])
        request.session['name'] = "test"  # more on session below
        print("*"*50)
        return redirect("/")
    else:
        return redirect("/")

def show(request, num):
    return HttpResponse(f"placeholder to display blog {num}")

def edit(request, num):
    return HttpResponse(f"placeholder to edit blog {num}")

def destroy(request, num):
    return redirect(index)