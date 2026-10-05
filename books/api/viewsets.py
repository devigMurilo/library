from rest_framework import viewsets
from books.models import Books
from books.models import Authors
# Cada arquivo só enxerga o que importa: o serializer precisa ser importado explicitamente
from books.api.serializers import BooksSerializer
from books.api.serializers import AuthorsSerializer


class BooksViewSet(viewsets.ModelViewSet):
    serializer_class = BooksSerializer
    queryset = Books.objects.all()

class AuthorsViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorsSerializer
    queryset = Authors.objects.all()
