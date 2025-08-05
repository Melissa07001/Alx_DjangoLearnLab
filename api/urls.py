from django.urls import path
<<<<<<< HEAD
from .views import (
    AuthorListCreateView, AuthorDetailView,
    BookListCreateView, BookDetailView
)

urlpatterns = [
    path('authors/', AuthorListCreateView.as_view(), name='author-list'),
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),
    path('books/', BookListCreateView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
=======
from .views import hello

urlpatterns = [
    path('hello/', hello),
>>>>>>> c44adeb1cd238ee62f92fa0072aa93fd5902541e
]
