from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
#from . models import UserDetails

#from .models import UserDetails
#from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput,TextInput

# class CustomLoginForm(AuthenticationForm):
#     pass  # This uses the default form fields for username and password

class CreateUserForm(UserCreationForm):
   

    class Meta:



        model= User

        fields = ['username','email','password1']
    
class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

