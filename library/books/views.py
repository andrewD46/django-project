from books.models import Book
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from books.serializers import BookListSerializer, BookDetailSerializer


class BooksList(viewsets.mixins.ListModelMixin, viewsets.mixins.RetrieveModelMixin, viewsets.mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Book.objects.all()
    serializer = BookListSerializer
    serializer_classes = {'list': BookListSerializer, 'retrieve': BookDetailSerializer, 'create': BookDetailSerializer}

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.serializer)

    def get(self, request):
        return self.list(request)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_book(self):
        book_id = self.kwargs.get('id')
        return get_object_or_404(Book, pk=book_id)
