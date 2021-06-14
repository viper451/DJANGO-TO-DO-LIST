from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    branch=(
		('COMPLETE','COMPLETE'), 
		('INCOMPLETE','INCOMPLETE')
	)
    type=( 
    ('-------','-------'),  
		('GROCERY','GROCERY'), 
		('MOVIE','MOVIE'),
    ('HOUSEHOLD','HOUSEHOLD'), 
		('HEALTH','HEALTH'),
    ('SOCIAL','SOCIAL'),
    ('OTHERS','OTHERS')
    
	)
    username = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="todolist", null=True,blank=True)
    title = models.CharField(unique=True,max_length=200 ,default='SOME STRING')
    created = models.DateTimeField(auto_now_add=True)
    tasktype=models.CharField(max_length=200,choices=type,default='-------')
    completetask=models.CharField(max_length=200,choices=branch,default='INCOMPLETE')

    def __str__(self):
      return self.title

