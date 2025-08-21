from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm

# Create your views here.
def index(request):
    return render(request, 'books/index.html')

def book_list(request):
    q = request.GET.get('q', '').strip()
    sort = request.GET.get('sort', 'date')
    qs = Book.objects.filter(owner=request.user)
    if q:
        qs = qs.filter(Q(title__icontains=q) | Q(author__icontains=q))
    qs = qs.order_by('title') if sort == 'title' else qs.order_by('-date_read', 'title')
    return render(request, 'books/book_list_html', {'books': qs, 'q': q, 'sort': sort})

def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book updated.')
            return redirect('book_list')
        else:
            form = BookForm(instance=book)
        return render(request, 'books/book_form.html', {'form': form})

def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk, owner=request.user)
    if request.method == 'POST':
        book.delete()
        message.info(request, 'Book delete.')
        return redirect('book_list')
    return render(request, books/book_confirm_delete.html', {'book': book})