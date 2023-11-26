from django.urls import path
from . import views

urlpatterns = [
    path('ogrenci/', views.ogrenci, name='ogrenci'),
    path('student/', views.ogrenci, name='ogrenci'),
    path('deneme/', views.deneme, name='deneme'),
    path('ders/', views.ders, name='dersler'),
    path('degiskenler/', views.degiskenler, name='01_degiskenlerkonusu'),
    path('degiskenler2/', views.degiskenler2, name='02_modeldendegiskenaktarma'),
    path('ogrencilerilistele/', views.listele, name='listele'),
    path('ogrencilerilistelek/', views.listelek, name='listelek'),
    path('ogretmenlistele/', views.listeleOgretmen, name='listeleOgretmen'),
    path('ogrencilerilistele/detay/<int:id>', views.detay, name='detay'),
    path('ogrencilerilistele/guncelle/<int:id>', views.guncelle, name='CRUD'),
    path('ogrencilerilistele/duzenle/<int:id>/', views.guncelle, name='guncelle_ogrenci'),  # Örnek güncelleme URL deseni
    path('ogrencilerilistele/sil/<int:id>', views.sil, name='detay'),
    # ursl.py dosyasına eklenecek satır.
    path('denemeif/', views.denemeiff, name='komutlar'),
    path('denemefor/', views.denemeforf, name='komutlar'),
    path('denemeforvt/', views.denemeforvtf, name='komutlar'),
    path('ogrenciekle/', views.ogrenci_kaydet, name='CRUD'),

]
