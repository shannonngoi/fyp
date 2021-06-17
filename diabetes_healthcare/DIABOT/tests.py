import pymongo
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from pymongo import MongoClient
from .forms import CreateUserForm, LoginForm

# Create your views here.

cluster = MongoClient('mongodb+srv://admin:passwordpassword@cluster0.wbq4q.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db = cluster['DIABOT']
collection = db['patient']

post = {"_medicalID" : 0 , "firstName": "tim", "lastName":"Ng"}
collection.insert_one(post)

def register(request):
    if request.user.is_athenticated:
        return redirect('homepage')
    else:
        form = CreateUserForm()
        if request.method =='POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request,'Create User Succesfully'+user )
                return redirect('login')

        context = {'form':form}
        return render(request, 'diabot/register.html',context)

@login_required(login_url='login')
def login(request):
    if request.user.is_athenticated:
        return redirect('homepage')
    else:
        if request.method =='POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('homepage')
            else:
                messages.info(request, 'Username or Password is INCONRRECT')
                

        context = {}
        return render(request,'diabot/login.html',context)    


def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def homepage(request):
    context ={
        
    }
    return render(request,'diabot/homepage.html', context)


 