from django.contrib.auth.models import User
from django.db import models
from .models import User
# Create your models here.

class LiteraryGenre(models.Model):
  tittle = models.CharField(max_length=255)


class Editor(models.Model):
  name = models.CharField(max_length=255)
  email = models.CharField(max_length=255)


class Book(models.Model):
  in_stock = models.BooleanField()
  user = models.ForeignKey(User, on_delete=models.PROTECT)
  tittle = models.CharField(max_length=255)
  page_count = models.IntegerField()
  author = models.CharField(max_length=255)
  literary_genre = models.ForeignKey(LiteraryGenre, on_delete=models.PROTECT)
  editor = models.ForeignKey(Editor, on_delete=models.PROTECT)