from rest_framework.generics import  ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Genre, Book
from .serializers import GenreSerializer, BookSerializer

class GenreListCreateAPIView(ListCreateAPIView):

    def get_queryset(self):
        return Genre.objects.all()

    def get_serializer_class(self):
        return GenreSerializer


class GenreRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    lookup_field = "pk"
    lookup_url_kwarg = "genre_id"

    def get_queryset(self):
        return Genre.objects.all()

    def get_serializer_class(self):
        return GenreSerializer


class BookListCreateAPIView(ListCreateAPIView):

    def get_queryset(self):
        genre_id = self.kwargs.get("genre_id")
        books = Book.objects.select_related("genre")
        if genre_id:
            books = books.filter(genre_id=genre_id)
        return books

    def get_serializer_class(self):
        return BookSerializer


class BookRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    lookup_field = "pk"
    lookup_url_kwarg = "book_id"

    def get_queryset(self):
        return Book.objects.select_related("genre")

    def get_serializer_class(self):
        return BookSerializer