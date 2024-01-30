from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home_process_function(request):
    # return HttpResponse('<h1>This is future home page</h1>')
    return render(request, 'layouts/home.html')
