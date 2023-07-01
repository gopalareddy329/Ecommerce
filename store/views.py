from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def store(request):
    return render(request,'store/store.html')

def loginpage(request):
    return render(request,'store/loginpage.html')

def signuppage(request):
    return render(request,'store/signuppage.html')


#@login_required(login_url='loginpage')
def cart(request):
    return render(request,'store/cart.html',{'no':2})


#@login_required(login_url='loginpage')
def checkout(request):
    return render(request,'store/checkout.html')


#@login_required(login_url='loginpage')
def account(request):
    return render(request,'store/account.html')


def searchpage(request):
    return render(request,'store/searchpage.html')


def productpage(request,id):
    return render (request,'store/productpage.html')

