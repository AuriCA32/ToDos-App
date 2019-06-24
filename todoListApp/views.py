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
            print(f)
            print("User registration failed")
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

"""
@login_required(login_url='/login/')
def index(request): #the index view
    todos = Todo.objects.all() #quering all todos with the object manager
    if request.method == "POST": #checking if the request method is a POST
        if "taskAdd" in request.POST: #checking if there is a request to add a todo
            title = request.POST["description"] #title
            date = str(request.POST["date"]) #date
            category = request.POST["category_select"] #category
            content = title + " -- " + date + " " + category #content
            Todo = Todo(title=title, content=content, due_date=date, category=Category.objects.get(name=category))
            Todo.save() #saving the todo 
            return redirect("/") #reloading the page
        if "taskDelete" in request.POST: #checking if there is a request to delete a todo
            checkedlist = request.POST.getlist("checkedbox") #checked todos to be deleted
            for todo_id in checkedlist:
                todo = Todo.objects.get(id=int(todo_id)) #getting todo id
                todo.delete() #deleting todo
        if "taskReady" in request.POST: #checking if there is a request to delete a todo
            checkedlist = request.POST.getlist("checkedbox") #checked todos to be deleted
            for todo_id in checkedlist:
                todo = Todo.objects.get(id=int(todo_id)) #getting todo id
                todo.status = 2
                todo.save() #deleting todo
        if "taskPending" in request.POST: #checking if there is a request to delete a todo
            checkedlist = request.POST.getlist("checkedbox")
            for todo_id in checkedlist:
                todo = Todo.objects.get(id=int(todo_id))
                todo.status = 1 #getting todo id
                todo.save() #deleting todo
    return render(request, "index.html", {"todos": todos, "categories":categories})
    """