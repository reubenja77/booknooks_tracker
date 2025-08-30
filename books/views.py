from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm

# Create your views here.
def index(request):
    """Landing page"""
    return render(request, 'books/index.html')

def signup(request):
    """Registration"""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Welcome! Your account was created.')
            return redirect('book_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def book_list(request):
    """List only current user's books (Must-Have)"""
    q = (request.GET.get('q') or '').strip()
    books = Book.objects.filter(owner=request.user)
    if q:
        books = books.filter(Q(title__icontains=q) | Q(author__icontains=q))
    return render(request, 'books/book_list.html', {'books': books, 'q': q})

@login_required
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.owner = request.user
            book.save()
            messages.success(request, 'Book added successfully.')
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'books/book_form.html', {'form': form})

@login_required
def book_update(request, pk):
    """Edit existing book owned by current user (Must-Have)"""
    book = get_object_or_404(Book, pk=pk, owner=request.user)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book updated.')
            return redirect('book_list')
        messages.error(request, 'Please fix the errors below.')
    else:
        form = BookForm(instance=book)
    return render(request, 'books/book_form.html', {'form': form, 'is_edit': True, 'book': book})

@login_required
def book_delete(request, pk):
    """Delete a book owned by current user (Must-Have)"""
    book = get_object_or_404(Book, pk=pk, owner=request.user)
    if request.method == 'POST':
        book.delete()
        messages.success(request, 'Book deleted.')
        return redirect('book_list')
    return render(request, 'books/book_confirm_delete.html', {'book': book})