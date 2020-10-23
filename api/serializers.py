from rest_framework import serializers
from .models import Book
from .models import Editor
from .models import LiteraryGenre
from django.contrib.auth.models import User


class SerializerUser(serializers.ModelSerializer):
  model = User
  fields = ('__all__')

class SerializerBook(serializers.ModelSerializer):
  model = Book
  fields = ('__all__')
  
class SerializerEditor(serializers.ModelSerializer):
  model = Editor
  fields = ('__all__')

class SerializerLiteraryGenre(serializers.ModelSerializer):
  model = LiteraryGenre
  fields = ('__all__')