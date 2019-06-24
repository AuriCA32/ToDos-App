from django.shortcuts import render
from .models import Todo
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render
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

def menu(request):
    return render(request, 'menu.html') 

@login_required(login_url='/login/')
def index(request): #the index view
    TaskList = Todo.objects.all()
    return render(request, 'index.html', { 'tasklist' : TaskList})

@login_required(login_url='/login/')
def createTask(request):
    if request.method == 'POST':
        f = TodoForm(data=request.POST)
        if f.is_valid():
            f.save()
            return HttpResponseRedirect('/')
        else:
            print(f)
            for field in f:
                for error in field.errors:
                    messages.error(request, error)
    else: 
        f = TodoForm()
    return render(request, 'forms.html', {'form': f, 'pageTitle': "Crear nueva tarea"})