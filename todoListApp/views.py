from django.shortcuts import render
from .models import Todo
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'index.html'

def LogIn(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        return HttpResponseRedirect('/menu')
    """
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            #user = authenticate(username=username, password=password)
            #if user is not None:
            #    print(user)
                #login(request, user)
                #return HttpResponseRedirect('/post/')
            #else:
            #    print('User not found')
        else:
            # If there were errors, we render the form with these
            # errors
            #return render(request, 'tilweb/login.html', {'form': form}) 
    """

def menu(request):
    return render(request, 'menu.html') 

"""
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