from django.urls import path

from .views import GenreListAPIView, BookListAPIView, GenreDetailAPIView


urlpatterns = [
    path('genres/', GenreListAPIView.as_view()),
    path('genres/<int:genre_id>', GenreDetailAPIView.as_view()),
    path('books/', BookListAPIView.as_view()),
    path('books/<int:genre_id>', BookListAPIView.as_view()),
]