from django.shortcuts import render
from django.shortcuts import redirect
from todoapp.forms import TodoCreateForm,UserRegistrationForm,LoginForm
from .models import Todos
from django.contrib.auth import authenticate,login as djangologin
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request,"home.html")

def index(request):
    return render(request,"index.html")


def create_todo(request):
    if request.method=="GET":

        form=TodoCreateForm(initial={'username':request.user})
        context={}
        context["forms"]=form
        return render(request,"createtodo.html",context)
    elif request.method=="POST":

        form=TodoCreateForm(request.POST)
        if form.is_valid():
            taknm=form.cleaned_data.get("taskname")
            user=form.cleaned_data.get("username")
            status=form.cleaned_data.get("status")
            todo=Todos(task_name=taknm,status=status,user=user)
            todo.save()
            return render(request,"index.html")

#todo=Todos.objects.all()
def list_all_todo(request):
        todos=Todos.objects.all()
        context={}
        context["todos"]=todos
        return render(request,"listalltodo.html",context)

def update_todo(request,id):

    todo=Todos.objects.get(id=id)
    instance={
        "taskname":todo.taskname,
        "username":todo.username,
        "status":todo.status
    }
    form = TodoCreateForm(initial=instance)
    context = {}
    context["form"] = form
    if request.method=="POST":
        form=TodoCreateForm(request.POST)
        if form.is_valid():
            task_name=form.cleaned_data.get("taskname")
            user=form.cleaned_data.get("username")
            status=form.cleaned_data.get("status")
            todo.task_name=task_name
            todo.user_name=user
            todo.status=status
            todo.save()
            return redirect("list")
    return render(request, "edittodo.html", context)

def delete_todo(request,id):
    todo=Todos.objects.get(id=id)
    todo.delete()
    return redirect("list")


def registration(request,*args,**kwargs):
    form=UserRegistrationForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            #messages.error(request,"registration failed")
            context["form"]=form
            return render(request, "registration.html", context)
    return render(request,"registration.html",context)

def signin(request,*args,**kwargs):
    form=LoginForm()
    context ={}
    context["form"] = form
    if request.method=="POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(request,username=username,password=password)
            if user:
                djangologin(request,user)
                return render(request,"index.html")
    return render(request,"login.html",context)
