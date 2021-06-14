from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import *
from django.contrib import  messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
from .filters import  TaskFilter
# Create your views here.

def loginPage(request):
    if request.method == 'POST':
       username=request.POST.get('username')
       password=request.POST.get('password')

       user=authenticate(request,username=username,password=password)

       if user is not None:
           login(request,user)
           return redirect('list')
       else:
           messages.info(request,"Username OR PASSWORD INCORRECT")
    return render(request,'tasks/login.html')

def registerPage(request):
	
     form=CreateUserForm()

     if request.method =='POST':
       form = CreateUserForm(request.POST)
       if form.is_valid():
          form.save()
          user =form.cleaned_data.get('username')
          
          messages.success(request,"ACCOUNT CREATED successfully of "+ user)
          return redirect('login')
		



     context = {'form':form}
     return render(request,'tasks/registeration.html',context)

def logoutUser(request):
	logout(request)
	return redirect('login')


@login_required(login_url='login')
def index(request):
    user=request.user
   
    tasks = Task.objects.filter(username=user)
    form = TaskForm()
     
    if request.method =='POST':
	    form = TaskForm(request.POST)
   
	    if form.is_valid():
		     form.save()   
	    messages.success(request,"ALLOWEED")	
	    return redirect('list')

    completed_tasks=Task.objects.filter(completetask='COMPLETE').filter(username=user).count()
    uncompleted_tasks=Task.objects.filter(completetask='INCOMPLETE').filter(username=user).count()
    left_task=Task.objects.filter(username=user).count()
    duedate=datetime.today() + timedelta(days=20)
  
    context = {'tasks':tasks,'form':form,'completed_tasks':completed_tasks,'uncompleted_tasks':uncompleted_tasks,'left_task':left_task,'duedate':duedate}
    return render(request, 'tasks/list.html', context)


@login_required(login_url='login')
def add_task(request):
 
    form = TaskForm()
    if request.method =='POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        task=Task.objects.filter(title=form['title'].value())    
        task.update(username=request.user)  
        return redirect('list')    

    context = {'form':form}
    return render(request,'tasks/add.html',context)    

@login_required(login_url='login')
def updateTask(request, pk):
	task = Task.objects.get(id=pk)

	form = TaskForm(instance=task)

	if request.method == 'POST':
		form = TaskForm(request.POST, instance=task)
		if form.is_valid():
			form.save()
			return redirect('list')

	context = {'form':form}

	return render(request, 'tasks/update_task.html', context)

@login_required(login_url='login')
def deleteTask(request, pk):
	item = Task.objects.get(id=pk)

	if request.method == 'POST':
		item.delete()
		return redirect('list')

	context = {'item':item}
	return render(request, 'tasks/delete.html', context)



