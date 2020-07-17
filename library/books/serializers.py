from books.models import Book
from rest_framework import serializers


class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'author_name')


class BookDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'author_name', 'description')
