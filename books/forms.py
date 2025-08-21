from django import forms
from .models import Book

class Bookform(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'authos', 'description', 'date_read']
        widgets = {'date_read': forms.DateInput(attrs={'type': 'date'})}