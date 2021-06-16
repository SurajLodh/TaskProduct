from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('product/', views.Add_Product, name = 'product'),
    path('products/', views.All_Product, name = 'products'),
]