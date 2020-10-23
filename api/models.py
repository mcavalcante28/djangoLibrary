from django.db import models
from .models import User
# Create your models here.

class Book(models.Model):
  tittle = models.CharField(max_length=255)
  page_count = models.IntegerField()
  author = models.CharField(max_length=255)
  literary_genre = models.ForeignKey(LiteraryGenre, on_delete=models.PROTECT)
  editor = models.ForeignKey(Editor, on_delete=models.PROTECT)


class LiteraryGenre(models.Model):
  tittle = models.CharField(max_length=255)


class Editor(models.Model):
  name = models.CharField(max_length=255)
  email = models.CharField(max_length=255)