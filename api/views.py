from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import Book
from .models import Editor
from .models import LiteraryGenre
from .serializers import SerializerBook
from .serializers import SerializerEditor
from .serializers import SerializerLiteraryGenre
from .serializers import SerializerUser



class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = SerializerUser

class BookViewSet(viewsets.ModelViewSet):
  queryset = Book.objects.all()
  serializer_class = SerializerBook

class EditorViewSet(viewsets.ModelViewSet):
  queryset = Editor.objects.all()
  serializer_class = SerializerEditor

class LiteraryGenreViewSet(viewsets.ModelViewSet):
  queryset = LiteraryGenre.objects.all()
  serializer_class = SerializerLiteraryGenre
