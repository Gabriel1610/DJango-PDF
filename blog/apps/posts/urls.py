from django.urls import path
from .views import index, posts

urlpatterns = [
    path('posts/', posts, name = 'posts'),
]