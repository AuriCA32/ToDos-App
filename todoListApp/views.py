from django.shortcuts import render
from .models import Todo
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import TodoForm

def SignUp(request):
    if request.method == 'POST':
        f = UserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully, please log in')
        else:
            for field in f:
                for error in field.errors:
                    messages.error(request, error)
    else:
        f = UserCreationForm()
    return render(request, 'signup.html', {'form': f})

def LogIn(request):
    if request.method == 'POST':
        f = AuthenticationForm(request=request, data=request.POST)
        if f.is_valid():
            username = f.cleaned_data.get('username')
            password = f.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                messages.error(request,'User does not exist in database.')
        else:
            messages.error(request,'Please enter a correct username and password. Note that both fields may be case-sensitive.')
    else: 
        f = AuthenticationForm()
    return render(request, 'login.html', {'form': f})

def LogOut(request):
    logout(request)
    return HttpResponseRedirect("/")

@login_required(login_url='/login/')
def index(request): #the index view
    TaskList = Todo.objects.all().order_by('id')
    return render(request, 'index.html', { 'tasklist' : TaskList})

@login_required(login_url='/login/')
def createTask(request):
    if request.method == 'POST':
        f = TodoForm(data=request.POST)
        if f.is_valid():
            f.save()
            return HttpResponseRedirect('/')
        else:
            for field in f:
                for error in field.errors:
                    messages.error(request, error)
    else: 
        f = TodoForm()
    return render(request, 'forms.html', {'form': f, 'pageTitle': "Crear nueva tarea"})

@login_required(login_url='/login/')
def editTask(request):
    given_id = int(request.path.split("_")[1])
    instance = get_object_or_404(Todo,id=given_id)
    f = TodoForm(request.POST or None, instance=instance)
    if request.method=="POST":
        if f.is_valid():
            f.save()
            return HttpResponseRedirect('/')
        else:
            for field in f:
                for error in field.errors:
                    e = field.label+": "+error
                    messages.error(request, e)
    try:
        form2 = {
            'title' : 1 if (instance.title!=None and instance.title!="") else 0,
            'body'  : 1 if (instance.body!=None and instance.body!="") else 0,
            'status' : 1 if instance.status==1 else 0,
        }
    except:
        form2 = {}
    print(form2)
    return render(request, 'forms.html', {'form': f, 'pageTitle': "Editar tarea", 'type' : 1, 'form2' : form2})

@login_required(login_url='/login/')
def deleteTask(request):
    given_id = int(request.path.split("_")[1])
    try:
        get_object_or_404(Todo,id=given_id).delete()
        return HttpResponseRedirect('/')
    except:
        messages.error(request,"No valid task is selected, no task will be deleted.")
        index(request)
    

@login_required(login_url='/login/')
def markCompleteTask(request):
    given_id = int(request.path.split("_")[1])
    instance = get_object_or_404(Todo,id=given_id)
    instance.status=0
    instance.save()
    return HttpResponseRedirect('/')

def error_404_view(request, exception):
    data = {"name": "ThePythonDjango.com"}
    return render(request,'404.html', data)