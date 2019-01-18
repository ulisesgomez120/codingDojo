from django.shortcuts import render, redirect
from .models import Product
from ..orders.models import Order
# Create your views here.
def index(req):
    context = {
        "items": Product.objects.all()
    }
    return render(req, 'products/index.html', context)

def process(req):
    if req.method == 'POST':
        req.session["total"] = Order.objects.total_price(req.POST)
        return redirect('/checkout')
    else:
        return redirect('/')

def checkout(req):
    return render(req, 'products/checkout.html')
