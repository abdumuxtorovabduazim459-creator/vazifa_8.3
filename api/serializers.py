from rest_framework import serializers

from .models import Genre, Book


class GenreSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    description = serializers.CharField(required=False, allow_null=True, allow_blank=True)

    def validate_name(self, value):
        genres = Genre.objects.filter(name=value)
        if self.instance:
            genres = genres.exclude(pk=self.instance.pk)
        if genres.exists():
            raise serializers.ValidationError()
        return value

    def create(self, validated_data):
        return Genre.objects.create(**validated_data)

    def update(self, instance: Genre, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.description = validated_data.get("description", instance.description)
        instance.save()
        return instance


class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    author = serializers.CharField(max_length=255)
    pages = serializers.IntegerField(default=100)
    published_year = serializers.IntegerField(default=2020)
    genre_id = serializers.IntegerField(required=False, allow_null=True)

    def validate_genre_id(self, value):
        if value is not None and not Genre.objects.filter(pk=value).exists():
            raise serializers.ValidationError("Genre mavjud emas!!")
        return value

    def create(self, validated_data):
        return Book.objects.create(**validated_data)

    def update(self, instance: Book, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.author = validated_data.get("author", instance.author)
        instance.pages = validated_data.get("pages", instance.pages)
        instance.published_year = validated_data.get("published_year", instance.published_year)
        instance.genre_id = validated_data.get("genre_id", instance.genre_id)
        instance.save()
        return instance
