from rest_framework import serializers
from .models import Author, Genre, Book

# UYGA VAZIFA: serializers.ModelSerializer serializers.Serializer ni o'rganish va farqini tushunish

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"
        

class BookSerializer(serializers.ModelSerializer):
    # author = AuthorSerializer(read_only=True)
    # genre = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = "__all__"
        read_only_fields = ('author', 'genre')
        
    