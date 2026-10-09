from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from .models import Genre, Book
from .serializers import  GenreSerializer, BookSerializer



class GenreListAPIView(APIView):
    def get(self, request: Request):
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data)

    def post(self, request: Request):
        serializer = GenreSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class GenreDetailAPIView(APIView):
    def get(self, request: Request, pk: int):
        genre = Genre.objects.filter(pk=pk).first()
        if genre is None:
            return Response( status=status.HTTP_404_NOT_FOUND)
        return Response(GenreSerializer(genre).data)

    def put(self, request: Request, pk: int):
        genre = Genre.objects.filter(pk=pk).first()
        if genre is None:
            return Response( status=status.HTTP_404_NOT_FOUND)
        serializer = GenreSerializer(genre, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def patch(self, request: Request, pk: int):
        genre = Genre.objects.filter(pk=pk).first()
        if genre is None:
            return Response( status=status.HTTP_404_NOT_FOUND)
        serializer = GenreSerializer(genre, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request: Request, pk: int):
        genre = Genre.objects.filter(pk=pk).first()
        if genre is None:
            return Response( status=status.HTTP_404_NOT_FOUND)
        genre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BookListAPIView(APIView):
    def get(self, request: Request, genre_id: int = None):
        if genre_id:
            books = Book.objects.filter(genre_id=genre_id)
        else:
            books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request: Request):
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class BookDetailAPIView(APIView):
    def get(self, request: Request, pk: int):
        book = Book.objects.filter(pk=pk).first()
        if book is None:
            return Response( status=status.HTTP_404_NOT_FOUND)
        return Response(BookSerializer(book).data)

    def put(self, request: Request, pk: int):
        book = Book.objects.filter(pk=pk).first()
        if book is None:
            return Response( status=status.HTTP_404_NOT_FOUND)
        serializer = BookSerializer(book, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def patch(self, request: Request, pk: int):
        book = Book.objects.filter(pk=pk).first()
        if book is None:
            return Response( status=status.HTTP_404_NOT_FOUND)
        serializer = BookSerializer(book, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request: Request, pk: int):
        book = Book.objects.filter(pk=pk).first()
        if book is None:
            return Response( status=status.HTTP_404_NOT_FOUND)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
