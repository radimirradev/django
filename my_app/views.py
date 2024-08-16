from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        'movies': ['Gladiator', 'TopGun', 'Casino']
    }
    return render(request, 'my_app/index.html', context)
def about(request):
    return render(request, 'my_app/about.html', {})

