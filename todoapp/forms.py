from django import forms
from django.forms import ModelForm
from .models import Todos
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

# we have to create a form for creating todoapp

class TodoCreateForm(forms.Form):
    taskname=forms.CharField()
    username=forms.CharField()
    options=(("completed","completed"),
            ("not completed","not completed"))
    status=forms.ChoiceField(choices=options)

#class TodoModelForm(forms.ModelForm):
   # class Meta:
       # model=Todos
       # field=["task_name","status","user"]

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=["first_name","last_name",'username',"email","password1","password2"]
        widgets={
            'first_name':forms.TextInput(attrs={"class":"form-control p-2"}),
            'last_name':forms.TextInput(attrs={"class":"form-control p-2"}),
            'username': forms.TextInput(attrs={"class": "form-control p-2"}),
            'email':forms.TextInput(attrs={"class":"form-control p-2"}),
            'password1':forms.PasswordInput(attrs={"class":"form-control p-2"}),
            'password2':forms.PasswordInput(attrs={"class": "form-control p-2"})
        }

