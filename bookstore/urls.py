from django.urls import path 
from django.shortcuts import render
from . import views

urlpatterns = [
    path('', views.listBooks, name='listBooks'),
    path('addbook', views.addNewBook, name='addNewBook'),
    path('updatebook', views.updateExistingBook, name='updateExistingBook'),

]