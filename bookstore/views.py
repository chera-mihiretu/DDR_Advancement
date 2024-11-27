from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import  *
from .forms import *
from django.urls import reverse
# Create your views here.

def listBooks(request):
    books = Book.objects.all()

    return render(request, 'bookstore/index.html', {'books': books})

def addNewBook(request):
    if request.method == "POST":

        

        form = BookForm(request.POST)
        
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
            
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
            
    comments = BookComments.objects.filter(book=book)


    return render(request, 'bookstore/detail.html', {'book': book, 'comments':comments})


def updateExistingBook(request):
    return render(request, 'bookstore/update.html')

def deleteBook(request, book_id):
    if request.method == "POST":
        book = get_object_or_404(Book, pk=book_id)
        book.delete()
        return redirect('listBooks')
    return render(request, 'bookstore/update.html')
def deleteComment(request, comment_id):
    book_id = BookComments.objects.get(pk=comment_id).book.id
    if request.method == "POST":
        comment = get_object_or_404(BookComments, pk=comment_id)
        comment.delete()
    url = reverse('detailBook', args=(book_id,))
    return redirect(url)