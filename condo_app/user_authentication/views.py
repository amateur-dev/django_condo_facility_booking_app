from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

def user_registeration(request):
    return HttpResponse("This will be the page through which a new user will be registered")

def user_login(request):
    return HttpResponse("This will be the page through which an existing user will be able to login")