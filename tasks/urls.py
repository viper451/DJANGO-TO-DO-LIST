from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
	path('list.html', views.index, name="list"), 
	path('update_task/<str:pk>/', views.updateTask, name="update_task"),
	path('delete/<str:pk>/', views.deleteTask, name="delete"),
	path('addtask/', views.add_task, name="add_task"),
	path('', views.loginPage, name="login"),
	path('register/', views.registerPage, name="register"),
	path('logout/', views.logoutUser, name="logout"),
	
]
