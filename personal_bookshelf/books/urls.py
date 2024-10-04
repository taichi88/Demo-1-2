from django.urls import path
from .views import (BookListView,BookDetailView, BookCreateView, BookUpdateView, BookDeleteView, AuthorListView, AuthroDetailView, AuthorCreateView, AuthorUpdateView, AuthorDeleteView)

urlpatterns = [
    path('book/list/', BookListView.as_view(), name='book_list'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('book/<int:pk>/edit/', BookUpdateView.as_view(), name='book_edit'),
    path('book/new/', BookCreateView.as_view(), name='Book_create'),
    path('book/<int:pk>/delete', BookDeleteView.as_view(), name='book_delete'),

    path('author/list/', AuthorListView.as_view(), name='author_list'),
    path('author/<int:pk>/', AuthroDetailView.as_view(), name='author_detail'),
    path('author/<int:pk>/edit', AuthorUpdateView.as_view(), name='author_edit'),
    path('author/new/', AuthorCreateView.as_view(), name='Author_create'),
    path('author/<int:pk>/delete', AuthorDeleteView.as_view(), name='author_delete'),

]

