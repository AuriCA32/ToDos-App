from django.urls import path,re_path

from . import views


urlpatterns = [
    path('signup/', views.SignUp, name='signup'),
    path('login/', views.LogIn, name='login'),
    path('', views.index, name='index'),
    path('create/', views.createTask, name='create'),
    re_path(r'edit_*', views.editTask, name='edit'),
    re_path(r'delete_*', views.deleteTask, name='delete'),
    re_path(r'mark_*', views.markCompleteTask, name='markcomplete'),
]