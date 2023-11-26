from django.contrib import admin
from .models import Ogrenci

class OgrenciAdmin(admin.ModelAdmin):
  list_display = ("TC", "Adi", "Soyadi",)
  
admin.site.register(Ogrenci, OgrenciAdmin)
