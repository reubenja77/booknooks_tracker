from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description', 'date_read']
        widgets = {'date_read': forms.DateInput(attrs={'type': 'date'})
        }