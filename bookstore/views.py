from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def listBooks(request):
    return render(request, 'bookstore/index.html')

def addNewBook(request):
    return render(request, 'bookstore/insert.html')

def updateExistingBook(request):
    return render(request, 'bookstore/update.html')

def deleteBook(request):
    # return render(request, 'bookstore/delete.html')
    pass

def likeBook(request):
    pass

def commentOnBook(request):
    pass