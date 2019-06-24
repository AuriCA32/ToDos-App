from django.urls import path

from . import views


urlpatterns = [
    path('signup/', views.SignUp, name='signup'),
    path('login/', views.LogIn, name='login'),
    path('menu/', views.menu, name='menu'),
    path('', views.index, name='index'),
    path('create/', views.createTask, name='create'),
]