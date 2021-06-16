from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.Home),
    path('signup/', views.SignUp, name='signup'),
    path('login/', views.Login, name='login'),
    path('logout/', views.Logout, name='logout'),
    path('post/', views.Post_art, name='post'),
    path('all_post', views.Posts_All, name='all_post'),

]