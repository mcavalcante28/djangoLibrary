from django.contrib import admin
from .models import Book
from .models import Editor
from .models import LiteraryGenre


admin.site.register(Book)
admin.site.register(Editor)
admin.site.register(LiteraryGenre)

