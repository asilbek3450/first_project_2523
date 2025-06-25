from django.urls import path
from .views import (
    AuthorListCreateAPIView, AuthorDetailAPIView,
    GenreListCreateAPIView, GenreDetailAPIView,
    BookListCreateAPIView, BookDetailAPIView,
)

urlpatterns = [
    path('authors/', AuthorListCreateAPIView.as_view()),
    path('authors/<int:pk>/', AuthorDetailAPIView.as_view()),
    path('genres/', GenreListCreateAPIView.as_view()),
    path('genres/<int:pk>/', GenreDetailAPIView.as_view()),
    path('books/', BookListCreateAPIView.as_view()),
    path('books/<int:pk>/', BookDetailAPIView.as_view()),
]
