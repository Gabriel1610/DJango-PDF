from django.urls import path
# from .views import posts para poder llamar a una vista basada en funciones
from .views import *

app_name = 'apps.posts'

urlpatterns = [
    # path('posts/', posts, name = 'posts'), forma de llamar a una vista basada en funciones
    path('posts/', PostListView.as_view(), name = 'posts'), # forma de llamar a una vista basada en funciones
    path("posts/<int:id>/", PostDetailView.as_view(), name = 'post_individual'),
    path('posts/crear/', PostCreateView.as_view(), name = 'crear_post'),
    path('posts/categoria', CategoriaCreateView.as_view(), name = 'crear_categoria'),
    path('categoria/', CategoriaListView.as_view(), name='categoria_list'),
    path('categoria/<int:pk>/delete/', CategoriaDeleteView.as_view(), name='categoria_delete'),
    path('post/<int:pk>/modificar/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/eliminar/', PostDeleteView.as_view(), name='post_delete'),
    path('comentario/<int:pk>/editar/', ComentarioUpdateView.as_view(), name='comentario_editar'),
    path('comentario/<int:pk>/eliminar/', ComentarioDeleteView.as_view(), name='comentario_eliminar'),
    path('categoria/<int:pk>/posts/', PostsPorCategoriaView.as_view(), name='post_por_categoria'),
]