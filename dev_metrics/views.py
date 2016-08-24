from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from .forms import addMetrics

def index(request):
    assert isinstance(request, HttpRequest)
    return render(request, 'dev_metrics_dashboard.html')


def get_add_metrics(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = addMetrics(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # redirect to a new URL:
            return HttpResponseRedirect('/devmetrics/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = addMetrics()

    return render(request, 'add_metrics.html', {'form': form})        

