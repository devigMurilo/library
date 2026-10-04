from rest_framework import viewsets
from books.models import Books
# Cada arquivo só enxerga o que importa: o serializer precisa ser importado explicitamente
from books.api.serializers import BooksSerializer

class BooksViewSet(viewsets.ModelViewSet):
    serializer_class = BooksSerializer
    queryset = Books.objects.all()
