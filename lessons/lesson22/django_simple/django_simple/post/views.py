from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def post(request):
    return HttpResponse("<h1>This is post page<h1>")
