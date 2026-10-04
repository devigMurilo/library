from django.db import models
from uuid import uuid4


# Create your models here.


class Books(models.Model):
    id_book = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publication_date = models.DateField()
    editoras = models.CharField(max_length=100)
