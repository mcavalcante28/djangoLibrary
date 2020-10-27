from django.shortcuts import render
from rest_framework import viewsets, generics, authentication, permissions
from django.contrib.auth.models import User
from django.db.models import Count
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from .models import Book
from .models import Editor
from .models import LiteraryGenre
from .serializers import SerializerBook
from .serializers import SerializerEditor
from .serializers import SerializerLiteraryGenre
from .serializers import SerializerUser
from rest_framework.views import APIView
import json



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

class BooksPerGenre(APIView):
  def get(self, request):
    id_genre = request.query_params.get('id_genre')
    books = Book.objects.all().filter(literary_genre = id_genre)
    serializer = SerializerBook(books, many=True)
    return Response(serializer.data, status=200)

class BooksPerUser(APIView):
  def get(self, request):
    user_logged = request.user
    books = Book.objects.all().filter(user = user_logged)
    serializer = SerializerBook(books, many=True)
    return Response(serializer.data,status=200)

class BooksPerEditor(APIView):
  def get(self, request):
    id_editor = request.query_params.get('id_editor')
    books = Book.objects.all().filter(editor = id_editor)
    serializer = SerializerBook(books, many=True)
    return Response(serializer.data,status=200) 

class BooksInLibrary(APIView):
  def get(self, request):
    book_count = Book.objects.filter(in_stock = True).count()
    obj = {
      "count_books": book_count
    }
    return Response(obj, status=200)