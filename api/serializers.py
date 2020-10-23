from rest_framework import serializers
from .models import Book
from .models import Editor
from .models import LiteraryGenre
from django.contrib.auth.models import User


class SerializerUser(serializers.ModelSerializer):
  class Meta: 
    model = User
    fields = ('__all__')

class SerializerBook(serializers.ModelSerializer):
  class Meta:
    model = Book
    fields = ('__all__')
  
class SerializerEditor(serializers.ModelSerializer):
  class Meta:
    model = Editor
    fields = ('__all__')

class SerializerLiteraryGenre(serializers.ModelSerializer):
  class Meta:
    model = LiteraryGenre
    fields = ('__all__')