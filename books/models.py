from django.db import models
from uuid import uuid4
from django.utils import timezone
from django.core.exceptions import ValidationError

def validar_data_publicacao(publication_date):
    if publication_date > timezone.now().date():
        raise ValidationError("A data de publicação não pode ser no futuro.")

# Create your models here.
#funcao para adicionar o caminho da imagem do livro no banco de dados
def upload_image_book(instance, filename):
    return f'books/images/{instance.id_book}/{filename}'

class Books(models.Model):
    id_book = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=100)
    author = models.ForeignKey('Authors', on_delete=models.CASCADE)
    publication_date = models.DateField(validators=[validar_data_publicacao])
    publisher = models.CharField(max_length=100)
    image = models.ImageField(upload_to=upload_image_book, null=True, blank=True)

class Authors(models.Model):
    id_author = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=100)
    biography = models.TextField()
    birth_date = models.DateField()
    death_date = models.DateField(null=True, blank=True)