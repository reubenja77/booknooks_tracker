from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.book_list, name='book_list'),
    path('books/new/', views.book_create, name='book_create'),
    path('books/<int:pk>/update/', views.book_update, name='book_update'),
    path('books/<int:pk>/delete/', views.book_delete, name='book_delete'),    
    path('signup/', views.signup, name='signup'),
    #path('', views.BookListView.as_view(), name='index'),
    #path('', views.book_list, name='book_list'),
    #path('create/', views.book_create, name='book_create'),
]