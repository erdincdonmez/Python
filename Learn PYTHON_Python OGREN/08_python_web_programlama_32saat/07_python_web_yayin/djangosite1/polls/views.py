from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    print("<TITLE>CGI script output</TITLE>")
    print("<H1>This is my first CGI script</H1>")
    print("Hello, world!")
    return HttpResponse("Hello, world. You're at the polls index.")
