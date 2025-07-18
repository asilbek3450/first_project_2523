from django.urls import path
from .views import (
    AuthorAPIView, AuthorDetailAPIView,
    GenreListCreateAPIView, GenreDetailAPIView,
    BookListCreateAPIView, BookDetailAPIView,
)

urlpatterns = [
    path('authors/', AuthorAPIView.as_view(), name='authors'),
    path('authors/<int:pk>/', AuthorDetailAPIView.as_view(), name='authors'),
    path('genres/', GenreListCreateAPIView.as_view()),
    path('genres/<int:pk>/', GenreDetailAPIView.as_view()),
    path('books/', BookListCreateAPIView.as_view()),
    path('books/<int:pk>/', BookDetailAPIView.as_view()),
]
