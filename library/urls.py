from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.DefaultRouter()

router.register('users', views.UserViewSet)
router.register('books', views.BookViewSet)
router.register('genre', views.LiteraryGenreViewSet)
router.register('editor', views.EditorViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    path('genre/books', views.BooksPerGenre.as_view()),
    path('books/count', views.BooksInLibrary.as_view()),
    path('user/books', views.BooksPerUser.as_view())
]
