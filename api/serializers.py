from rest_framework import serializers

from .models import Genre, Book

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        exclude = []
        read_only_fields = ['id']
        extra_kwargs = {
            'name': {'min_length': 2},
            'description': {'required': False},
        }


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        exclude = []
        read_only_fields = ['id']
        extra_kwargs = {
            'pages': {'min_value': 1},
        }