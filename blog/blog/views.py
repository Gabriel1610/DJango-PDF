from django.shortcuts import render
from django.http import HttpResponseNotFound
from apps.posts.models import Post  # Asegúrate de que esta ruta sea correcta

def index(request):
    post_fijo = Post.objects.filter(id=5)  # Consulta el post con id=5
    otros_posts = Post.objects.exclude(id=5)  # Excluye el post con id=5 y consulta el resto
    posts = list(post_fijo) + list(otros_posts)  # Combina ambos conjuntos, con el post fijo primero
    return render(request, 'index.html', {'posts': posts})

def acercade(request):
    return render(request, 'acercade.html')

def pagina_404(request, exception):
    return HttpResponseNotFound('<h1>Página no encontrada</h1>')