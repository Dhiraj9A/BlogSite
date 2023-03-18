from django.shortcuts import render, redirect
from .models import Blog
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='login')
def index(request):
    blogs = Blog.objects.all()
    return render(request, 'index.html', {'blogs': blogs})

def single(request, pk):
    blog = Blog.objects.get(id=pk)
    return render(request, 'single.html', {'blog': blog})


def login(request):
    if request.method == "POST":
        username = request.POST['username'] 
        password = request.POST['password']  

        user = auth.authenticate(username=username, password=password)
        print(user)
        if user is not None: 
            auth.login(request, user)
            return redirect("home")   
        else: 
            messages.info(request, "Username or password is incorrect")
            return redirect("login")
    else: 
        return render(request, 'login.html')

def signup(request):
    if request.method == "POST":
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.info(request, "Username already exists")
            return redirect("signup")

        elif User.objects.filter(email=email).exists():
            messages.info(request, "Email is already in Use")
            return redirect("signup")

        else: 
            new_user = User(first_name=fname, last_name=lname, username=username, email=email, password=password)
            new_user.save()
            
            return redirect("login")

    else: 
        return render(request, 'signup.html') 

def logout(request):
    auth.logout(request)
    return redirect("login")

    