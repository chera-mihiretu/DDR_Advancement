from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import  *
from .forms import *
# Create your views here.

def listBooks(request):
    books = Book.objects.all()

    return render(request, 'bookstore/index.html', {'books': books})

def addNewBook(request):
    if request.method == "POST":

        title = request.POST.get('title')
        author = request.POST.get('author') 
        publication_date = request.POST.get('publication_date')
        pages = request.POST.get('pages')
        price = request.POST.get('price')
        genre = request.POST.get('genre')

        form = BookForm(title= title, author= author, publication_date= publication_date, pages= pages, price= price, genre= genre)

        if form.is_valid():
            form.save()
            return redirect('')
    else:
        form = BookForm()
    return render(request, 'bookstore/insert.html')

def detailBook(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == "POST":
        if 'like' in request.POST:
            book.likes += 1
            book.save()
        elif 'comment' in request.POST:
            comment = request.POST.get('comment')
            BookComments.objects.create(book=book, comment=comment)
            



    return render(request, 'bookstore/detail.html', {'book': book})


def updateExistingBook(request):
    return render(request, 'bookstore/update.html')

def deleteBook(request):
    # return render(request, 'bookstore/delete.html')
    pass
