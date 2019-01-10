from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    
    return render(request, 'survey_form/index.html')

def process(request):
    request.session['name'] = request.POST['first_name']
    request.session['language'] = request.POST['language']
    request.session['location'] = request.POST['location']
    return redirect('/result')

def result(request):

    return render(request, 'survey_form/results.html')