from django.db import models
from uuid import uuid4


# Create your models here.
#funcao para adicionar o caminho da imagem do livro no banco de dados
def upload_image_book(instance, filename):
    return f'books/images/{instance.id_book}/{filename}'

class Books(models.Model):
    id_book = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publication_date = models.DateField()
    editoras = models.CharField(max_length=100)
    image = models.ImageField(upload_to=upload_image_book, null=True, blank=True)