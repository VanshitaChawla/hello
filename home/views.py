from multiprocessing import AuthenticationError
from django.shortcuts import render,HttpResponse,redirect
from home.models import Contact
from home.models import Product
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout
# Create your views here.

def ecom(request):
    if request.user.is_anonymous:
        return redirect("/login")
    products=Product.objects.all()
    params={'product':products}
    return render(request,'ecom.html')
def about(request):
    return render(request,'about.html')
def blog(request):
    return render(request,'blog.html')
def cart(request):
    return render(request,'cart.html')
def product(request):
    return render(request,'product.html')
def about(request):
    return render(request,'about.html')

def shop(request):
    return render(request,'shop.html')
def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phoneno=request.POST.get('phoneno')
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email,phoneno=phoneno,desc=desc)
        contact.save()
        messages.success(request, 'Contact created')
    return render(request,'contact.html')
def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = Authentication(username=username, password=password)
        if user is not none:
            return redirect("/")
        else:
            return render(request,'login.html')

    return render(request,'login.html')
def logoutuser(request):
    logout(request)
    return redirect("/login")