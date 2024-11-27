from django.urls import path 
from django.shortcuts import render
from . import views

urlpatterns = [
    path('', views.listBooks, name='listBooks'),
    path('addbook', views.addNewBook, name='addNewBook'),
    path('updatebook', views.updateExistingBook, name='updateExistingBook'),
    path('detail/<int:book_id>', views.detailBook, name='detailBook'),
    path('comment/<int:book_id>', views.commentOnBook, name='commentOnBook'),
    path('like/<int:book_id>', views.likeBook, name='likeBook'),

]