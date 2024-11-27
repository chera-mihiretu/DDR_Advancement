# DDR_Advancement
This is the project that may contain DJango and React JS as well as docker container


# DATE NOV 22

### DJANGO TEMPLATE 
Whenever we are working on simple Project we can use templates to render the output of out backend operation.

Template -> Simple index with some extra sysntax of python 

The data are fitted into the html page through django 

For every application we might have a page for that we place our html files inside The app folder 

```bash
bookstore
├── admin.py
├── apps.py
├── forms.py
├── __init__.py
├── models.py
├── static
│   └── styles.css
├── templates
│   └── bookstore
│       ├── detail.html
│       ├── footer.html
│       ├── header.html
│       ├── index.html
│       ├── insert.html
│       └── update.html
├── tests.py
├── urls.py
└── views.py
```

In the above file the folder templates is placed in the app directory [templates] is necessary.

Then inside that we will again create a directory of the same name of the app This will help django the relevant page to the application.

Then the pages will go inside the /templates/[app_name]/

if you want to use css files for your pages you cannot use it directly that is why we need the static directory.


To use the css file in your page 

```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
        <link rel="stylesheet" href="{% static 'styles.css' %}">
    </head>
    <body>
    </body>
</html>
```

Dont forget to include 
```python 
# setttins.py
STATIC_URL = 'static/'
```

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




