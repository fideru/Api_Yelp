from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# Represents main page of any app
def index(request):
    return HttpResponse("What Upp Nyugga")
