from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

def index(request):
    assert isinstance(request, HttpRequest)
    return HttpResponse('Hello World!')
        

