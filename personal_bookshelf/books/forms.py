from django import forms
from .models import Author, Book




class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ["name", "surname", "personal_thoughts"]

    
class BookForm(forms.ModelForm):
    #ეს release_date იმისთვის რომ ძაან მარტივად რომ ჩამოშალოს დეითI ხელით რომ არმოგვიწიოს შეყვანა
    release_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'})) 
    class Meta:
        model = Book

        fields = ['title', 'description', 'author', 'genre', 'release_date', 'personal_thoughts']
