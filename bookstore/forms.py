from django import forms
from .models import *
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_date', 'pages', 'price', 'genre']
    
