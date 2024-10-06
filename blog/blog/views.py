from django.shortcuts import render

def index(request):
    current_url = request.path
    context = {
        'current_url': current_url,
    }
    return render(request, 'index.html', context)