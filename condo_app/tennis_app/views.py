from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello you are in the landing page of the tennis_app")