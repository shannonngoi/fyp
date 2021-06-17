
from django.shortcuts import render, redirect, get_object_or_404
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpResponse,HttpResponseRedirect
from  django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from pymongo import MongoClient
from django.contrib.auth.models import Group
from .forms import addUserForm
from .decorators import unauthenticated_user, allowed_users, patient_only

import pymongo
from django.conf import settings
cluster = MongoClient(settings.DB_NAME)

# First define the database name
db = cluster['DIABOT']

# Now get/create collection name (remember that you will see the database in your mongodb cluster only after you create a collection)
collection = db['DIABOT_adduser']
results = collection.find_one({"id":1})
print(results)

# Create your views here.
@unauthenticated_user
def register(request):
    
    # If this is a POST request then process the Form data
    if request.method =='POST':
        form = addUserForm(request.POST)
    
        # Check if the form is valid:
        if form.is_valid():
            user =form.save()
            #get data from the form typed by user
            firstname = form.cleaned_data.get('firstname')
            lastname = form.cleaned_data.get('lastname')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            gender = form.cleaned_data.get('gender')
            martial = form.cleaned_data.get('martial')
            
            context = {'form': form, 'firstname': firstname,'lastname':lastname, 'email':email,'password':password,'gender':gender,'martial':martial}
            group = Group.objects.get(name='patient')
            user.groups.add(group)

            #succesful create the user
            messages.success(request,'Create User Succesfully!' )
            return redirect('login', context)

        else:
            form=addUserForm()
            return render(request, 'diabot/register.html',{'form':form})

@unauthenticated_user
def login(request):
    if request.method =='POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user_obj = auth.authenticate(request, email=email, password=password)
        

        if user_obj is not None:
            # got issue cant go through the user_obj , user_objc got nothing!!!!
            messages.info(request, 'sasasasa')
            print (email)
    
            auth.login(request, user_obj) #user= object store email and password
            messages.info(request, 'succesfull')
            return redirect('homepage')

        else:
            
            messages.info(request, 'usename or Password is INCONRRECT')
            return redirect('login')
                
    context = {}
    return render(request,'diabot/login.html',context)    


def logoutUser(request):
    auth.logout(request)
    return redirect('login')

@login_required(login_url='login')
@patient_only
def homepage(request):
    context ={
        
    }
    return render(request,'diabot/homepage.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['medicalStaff'])
def medicalDashboard(request):
    context = {

    }
    return render(request, 'diabot/medicalDashboard.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['patient'])
def userDashboard(request):
    context = {

    }
    return render(request, 'diabot/userDashboard.html', context)


