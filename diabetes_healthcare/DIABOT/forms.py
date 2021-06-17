from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *
import pymongo
from django.conf import settings
from pymongo import MongoClient
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

# database connection
cluster = MongoClient(settings.DB_NAME)

# First define the database name
db = cluster['DIABOT']

# Now get/create collection name (remember that you will see the database in your mongodb cluster only after you create a collection)
collection = db['patient']


#trial to check accessibility
results = collection.find_one({"_id":3})
print(results)

class addUserForm(forms.ModelForm):
    class Meta:
        model = addUser
        fields = ['firstname','lastname','email','password','gender','martial']

'''
#add users
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
    #registerr models link to db
    #def save(request):
        #collection.insert(views.register.userprofile)
        #collection.insert(forms)
'''



# Register your models here.

