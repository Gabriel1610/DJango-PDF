from django.shortcuts import render
from .models import Post
from django.views.generic import ListView

# Create your views here.

# vista basada en funciones
def posts(request):
    posts = Post.objects.all()
    return render(request, 'posts.html', {'posts':posts})

# vista basada en clases
class PostListView(ListView):
    model = Post
    template_name = "post.html"
    context_object_name = "posts"