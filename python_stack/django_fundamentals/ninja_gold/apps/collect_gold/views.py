from django.shortcuts import render, redirect
import random
from time import strftime, localtime
# Create your views here.
def index(req):
    if "gold" not in req.session:
        req.session['gold'] = 0
    return render(req, 'collect_gold/index.html')

def process(req, location=''):
    if "activities" not in req.session:
        req.session['activities'] = []
    temp_list = req.session['activities']
    if location == "farm":
        amount = random.randint(10,20)
        when = strftime("%Y/%d/%m %I:%M %p", localtime())
        req.session['gold'] += amount
        req.session['color'] = "success"
        temp_list.append(f"You earned {amount} gold at the {location}! ({when})")
    if location == "cave":
        amount = random.randint(5,10)
        when = strftime("%Y/%d/%m %I:%M %p", localtime())
        req.session['gold'] += amount
        req.session['color'] = "success"
        temp_list.append(f"You earned {amount} gold at the {location}! ({when})")
    if location == "house":
        amount = random.randint(2,5)
        when = strftime("%Y/%d/%m %I:%M %p", localtime())
        req.session['gold'] += amount
        req.session['color'] = "success"
        temp_list.append(f"You earned {amount} gold at the {location}! ({when})")
    if location == "casino":
        amount = random.randint(-50,50)
        when = strftime("%Y/%d/%m %I:%M %p", localtime())
        req.session['gold'] += amount
        if amount >= 0:
            req.session['color'] = "success"
            temp_list.append(f"You won {amount} gold at the {location}! ({when})")
        if amount < 0:
            req.session['color'] = "danger"
            temp_list.append(f"You lost {abs(amount)} gold at the {location}! ({when})")
    
    print(req.session['activities'], req.session['gold'])
    
    return redirect('/')

def clear(req):
    req.session.clear()
    return redirect('/')