from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import TodoForm
from .models import Todo

def SignUp(request):
    return basicView(request,'signup.html',UserCreationForm,{})

def LogIn(request):
    if request.method == 'POST': #If POST user wants to login
        f = AuthenticationForm(request=request, data=request.POST)
        if f.is_valid():
            # Form is valid, try to authenticate user
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
    else: #If GET, user wants the form to type in the login data
        f = AuthenticationForm()
    return render(request, 'login.html', {'form': f})

def LogOut(request):
    logout(request)
    return HttpResponseRedirect("/")

@login_required(login_url='/login/')
def index(request):
    TaskList = Todo.objects.all().order_by('id')
    return render(request, 'index.html', { 'tasklist' : TaskList})

@login_required(login_url='/login/')
def createTask(request):
    return basicView(request,'forms.html',TodoForm,{'pageTitle': "Crear nueva tarea"},1)

@login_required(login_url='/login/')
def editTask(request):
    # Find the instance with id in path and create form
    instance = get_object_from_path(Todo,request.path)
    f = TodoForm(request.POST or None, instance=instance)
    # For rendering the template properly, form2 indicates the following:
    #   title : 1 if title is not empty string, else 0.
    #   body : 1 if body is not empty string, else 0.
    #   status : 1 if status is pending (1), else 0.
    try:
        form2 = {
            'title' : 1 if (instance.title!=None and instance.title!="") else 0,
            'body'  : 1 if (instance.body!=None and instance.body!="") else 0,
            'status' : 1 if instance.status==1 else 0,
        }
    except:
        form2 = {}
    # Create Context to merge with modelForm
    newContext = {
        'pageTitle': "Editar tarea",
        'type' : 1, 
        'form2' : form2
    }
    return basicView(request,'forms.html',TodoForm,newContext,2,f)

@login_required(login_url='/login/')
def deleteTask(request):
    get_object_from_path(Todo,request.path).delete()
    return HttpResponseRedirect('/')

@login_required(login_url='/login/')
def markCompleteTask(request):
    instance = get_object_from_path(Todo,request.path)
    instance.status=0
    instance.save()
    return HttpResponseRedirect('/')

def get_object_from_path(model,path):
    given_id = int(path.split("_")[1])
    return get_object_or_404(model,id=given_id)

def basicView(request,template,modelform,mergeWithContext,v_type=0,form=None):
    f=form
    if request.method == 'POST': # for POST request
        # If no form, then create one with request since method is POST
        if f==None:
            f = modelform(request.POST)
        #If valid save or give success message.
        if f.is_valid():
            f.save()
            if v_type!=0:
                return HttpResponseRedirect('/')
            else:
                messages.success(request, 'Account created successfully, please log in')
        #If not valid, get error messages
        else:
            for field in f:
                for error in field.errors:
                    # Only while edit, we need to specify field that gave error
                    if form:
                        e = field.label+": "+error
                    # Otherwise get just error message
                    else:
                        e = error
                    messages.error(request, e)
    else: # for GET request 
        # If no form, then create an empty one since method is GET
        if f==None:
            f = modelform()
    #Create context to render
    newContext = {**mergeWithContext,**{'form': f}}

    #Return
    return render(request, template, newContext)