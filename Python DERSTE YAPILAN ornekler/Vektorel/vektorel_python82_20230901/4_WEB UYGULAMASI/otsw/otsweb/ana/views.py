# from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader

def ana(request):
    template = loader.get_template('ana.html')
    return HttpResponse(template.render())

