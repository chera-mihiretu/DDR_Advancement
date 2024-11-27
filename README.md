# DDR_Advancement
This is the project that may contain DJango and React JS as well as docker container




# DATE NOV 27
### DJANGO CRUD OPERATION 

 - Today I have learned how to do CRUD operation using django 
 - I created and App called bookstore 
 - I created the following model 
    - ### Book
    - ### Comments

The Book Model has the following entities
#### Book 
 - title
 - author 
 - publication_date
 - pages
 - price
 - genre
 - likes 
The Comment Model Has the following entities
#### Comment 
 - primary_key
 - The comment 



## Here are The operations 

## [Inserting the Book](https://www.fundaofwebit.com/django/insert-data-into-database-in-django) 
 ```python 
# This will create a form for automatic filling 
from django import forms
from .models import *
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_date', 'pages', 'price', 'genre']

```

## Then we will create the form Object 

```python 
def saveForm(request):
    if request.method == "POST":
        ## you can do custom check over here for validation 
        form = BookForm(request.POST)
        
        if form.is_valid():
            form.save()
        else:
            # It will print the errors related to the inputs 
            print(form.errors)
            
    return render(request, 'bookstore/insert.html')
```

# [Deleting Data](https://www.fundaofwebit.com/django/delete-data-from-database-in-django)

To delete a data from the database we easily send the object id and 


```python 
def deleteBook(request, book_id):
    if request.method == "POST":
        book = get_object_or_404(Book, pk=book_id)
        book.delete()
        return redirect('listBooks')
    return render(request, 'bookstore/update.html')
```


This Will delete The model based on the provided ID through template 

# [Getting Data](https://www.fundaofwebit.com/django/fetch-data-from-database-in-django)

Data are also fetched through the id of the object 

```python 

def detailBook(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == "POST":
        # check if the request is post or not because we 
        # are only delete if the method is post 

        # and also we are gonna check the attribute of 
        # like and comment to do the corresponding operation 
        if 'like' in request.POST:
            # we weill update the books like 
            book.likes += 1
            book.save()
        elif 'comment' in request.POST:
            # creating the comment object with primary key of the current book 
            comment = request.POST.get('comment')
            BookComments.objects.create(book=book, comment=comment)
            
    comments = BookComments.objects.filter(book=book)


    return render(request, 'bookstore/detail.html', {'book': book, 'comments':comments})


```

# [Update Data](https://www.fundaofwebit.com/django/update-data-into-database)

Updating the object is also through object ID 

```python

def detailBook(request, book_id):
    # We get the object from the database 
    book = get_object_or_404(Book, pk=book_id)
    if request.method == "POST":
        if 'like' in request.POST:
            # we modify the required data
            book.likes += 1
            # we should save it on the database 
            # because we modified the object 
            book.save()
    return render(request, 'bookstore/detail.html', {'book': book, 'comments':comments})

```




