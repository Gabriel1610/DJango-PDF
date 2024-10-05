from django.urls import path
# from .views import posts para poder llamar a una vista basada en funciones
from .views import PostListView, PostDetailView
from . import views

urlpatterns = [
    # path('posts/', posts, name = 'posts'), forma de llamar a una vista basada en funciones
    path('posts/', PostListView.as_view(), name = 'posts'), # forma de llamar a una vista basada en funciones
    path("posts/<int:id>/", PostDetailView.as_view(), name = 'post_individual')
]