from django.http import HttpResponse
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>Saat ve tarih bilgisi: %s.</body></html>" % now
    return HttpResponse(html)
from django.shortcuts import render
from Blog.models import Gonderiler

def gonderi_goster(request , gonderi_id):
	Gonderi = Gonderiler.objects.get(id = gonderi_id)
	
	return render(request, "gonderi_goster.html", locals())
