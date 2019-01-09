from django.shortcuts import render
from time import gmtime, strftime
# Create your views here.
def index(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    print("--" *40, context)
    return render(request, 'page.html', context)