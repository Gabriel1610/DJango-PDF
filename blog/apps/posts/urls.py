from django.urls import path
# from .views import posts para poder llamar a una vista basada en funciones
from .views import PostListView, PostDetailView, PostCreateView, CategoriaCreateView

app_name = 'apps.posts'

urlpatterns = [
    # path('posts/', posts, name = 'posts'), forma de llamar a una vista basada en funciones
    path('posts/', PostListView.as_view(), name = 'posts'), # forma de llamar a una vista basada en funciones
    path("posts/<int:id>/", PostDetailView.as_view(), name = 'post_individual'),
    path('posts/', PostCreateView.as_view(), name = 'crear_posts'),
    path('posts/categoria', CategoriaCreateView.as_view(), name = 'crear_categoria'),
]