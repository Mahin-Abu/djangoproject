from django.shortcuts import render,redirect

from shop.models import Category

from shop.models import Product
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def allprodcat(request):
    c=Category.objects.all()
    return render(request,'category.html',{'c':c})
def allproducts(request,e):
    c = Category.objects.get(slug=e)
    p=Product.objects.filter(category__slug=e)
    return render(request,'products.html',{'p':p,'c':c})

def viewproduct(request,e):
    p=Product.objects.get(slug=e)
    return render(request,'detail.html',{'p':p})

def register(request):
    if(request.method=="POST"):
        u=request.POST['u']
        f=request.POST['f']
        l=request.POST['l']
        e=request.POST['u']
        p=request.POST['p']
        cp=request.POST['cp']
        if p==cp:
            u=User.objects.create_user(username=u,first_name=f,last_name=l,email=e,password=p)
            u.save()
            return user_login(request)
        else:
            messages.error(request,"PASSWORD MISSMATCH")
    return render(request,'register.html')

def user_login(request):
    if(request.method=="POST"):
        username=request.POST['u']
        password=request.POST['p']
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return allprodcat(request)
        else:
            messages.error(request,"Invalid user credentials")

    return render(request,'login.html')

@login_required
def user_logout(request):
    logout(request)
    return allprodcat(request)