from django.urls import path 
from django.shortcuts import render
from . import views

urlpatterns = [
    path('', views.listBooks, name='listBooks'),
    path('addbook', views.addNewBook, name='addNewBook'),
    path('updatebook', views.updateExistingBook, name='updateExistingBook'),
    path('detail/<int:book_id>', views.detailBook, name='detailBook'),
    path('delete/<int:book_id>', views.deleteBook, name='deleteBook'),
    path('deletecomment/<int:comment_id>', views.deleteComment, name='deleteComment'),


]