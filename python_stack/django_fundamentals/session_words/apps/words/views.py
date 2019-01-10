from django.shortcuts import render, redirect

# Create your views here.
def index(req):
    if "words" in req.session:
        context = {
            "words": req.session['words']
        }
    else:
        context = []
    return render(req, 'words/index.html', context)

def add(req):
    if 'big_text' not in req.POST:
        big = 0
    else:
        big = 1
    if 'words' not in req.session:
        req.session['words'] = []
    temp_list = req.session['words']
    temp_list.append({"word": req.POST['word'], "color": req.POST['color'], "big_text": big})
    req.session['words'] = temp_list
    return redirect('/')

def clear(req):
    req.session.clear()
    return redirect('/')