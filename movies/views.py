from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie

# Create your views here.

# Represents main page of any app
def index(request):
    movies = Movie.objects.all()
    return (render(request, 'index.html', {'movies': movies}))
#    output = ','.join(m.title for m in movies)
