from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class TaskForm(forms.ModelForm): 
	
	title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Add new task...'}))

	class Meta:
		model = Task
		fields =['title','completetask','tasktype']

class CreateUserForm(UserCreationForm):
    class Meta:
	    model = User
	    fields = ['username', 'email','password1','password2']
   

