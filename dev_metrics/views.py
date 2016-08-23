from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

def index(request):
    assert isinstance(request, HttpRequest)
    return render(request, 'dev_metrics_dashboard.html')
        

