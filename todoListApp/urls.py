from django.urls import path

from . import views


urlpatterns = [
    path('signup/', views.SignUp, name='signup'),
    path('login/', views.LogIn, name='login'),
    path('', views.menu, name='menu'),
]