from django import forms
from .models import Author, Book




class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ["name", "surname", "personal_thoughts"]

    
class BookForm(forms.ModelForm):
    class Meta:
        model = Book

        fields = ['title', 'description', 'author', 'genre', 'release_date', 'personal_thoughts']
