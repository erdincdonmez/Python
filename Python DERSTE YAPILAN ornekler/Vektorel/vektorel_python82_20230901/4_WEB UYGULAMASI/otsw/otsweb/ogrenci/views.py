from django.http import HttpResponse
from django.template import loader

def ogrenci(request):
    template=loader.get_template('ogrenci.html')

    return HttpResponse(template.render())

def deneme(request):
    template=loader.get_template('deneme.html')
    return HttpResponse(template.render())

def ders(request):
    template=loader.get_template('ders.html')
    return HttpResponse(template.render())

def degiskenler(request):
    template=loader.get_template('01_degiskenler.html')
    gonderilen = { # burada genelde gönderilen değişken adı olarak context kullanılır.
        'mesaj': 'Dersler sayfası',
    }
    return HttpResponse(template.render(gonderilen,request))


from .models import Ogrenci
from .models import Ogretmen

def degiskenler2(request):
  ogrencilistesi = Ogrenci.objects.all().values()
  template = loader.get_template('02_degiskenler.html')
  gonderilen = {
    'ogrenciler': ogrencilistesi,
  }
  return HttpResponse(template.render(gonderilen, request))


def listele(aa):
    

    # if aa.method == 'POST':
    #     form = OgrenciForm(aa.POST)
    #     if form.is_valid():
    #         # Form verileri işleme
    #         form.save()  # Veritabanına kaydetme
    # else:
    #         form = OgrenciForm()



    ogrenciliste = Ogrenci.objects.all()
    ogrenciliste1 = Ogrenci.objects.all().values()
    ogrenciliste2 = Ogrenci.objects.values_list('Adi')
    ogrenciliste3 = Ogrenci.objects.filter(Adi='Ensar').values()
    tmp = loader.get_template('ogrencilistesi.html')
    bb ={
        'abc' : ogrenciliste,
        'liste' : ogrenciliste1,
        'liste2' : ogrenciliste2,
        'liste3' : ogrenciliste3,
        # 'form': form,
    }
    return HttpResponse(tmp.render(bb, aa))




def listelek(request):
    ogrenciliste = Ogrenci.objects.all()
    template = loader.get_template('ogrencikartlistesi.html')
    context ={
        'abc' : ogrenciliste,
    }
    return HttpResponse(template.render(context, request))

def listeleOgretmen(request):
    listeOgretmen = Ogretmen.objects.all()
    template = loader.get_template('ogretmenlistesi.html')
    context ={
        'aktarilanOgretmenler' : listeOgretmen,
    }
    return HttpResponse(template.render(context, request))

def detay(request, id):
    item = Ogrenci.objects.get(id=id)
    template = loader.get_template('ogrencidetay.html')
    context = {
        'aktarilan': item,
    }
    return HttpResponse(template.render(context, request))

def sil(request, id):
    item = Ogrenci.objects.get(id=id)
    item.delete()
    return redirect('listele') #url name

    ogrenciliste = Ogrenci.objects.all()
    template = loader.get_template('ogrencilistesi.html')
    context ={
        'abc' : ogrenciliste,
    }
    return HttpResponse(template.render(context, "/ogrencilerilistele"))

def denemeiff(request):
  template = loader.get_template('denemeif.html')
  context = {
    'durum': 2,
  }
  return HttpResponse(template.render(context, request))

def denemeforf(request):
  liste = ["Elma","Armut","Kiraz"]
  template = loader.get_template('denemefor.html')
  giden = {
    'aktarilanListe': liste,
  }
  return HttpResponse(template.render(giden, request))  

def denemeforvtf(request):
  ogrenciListesi = Ogrenci.objects.all().values()
  template = loader.get_template('denemeforvt.html')
  context = {
    'aktarilanListe': ogrenciListesi,
  }
  return HttpResponse(template.render(context, request))  

from django import forms
from .models import Ogrenci

class OgrenciForm(forms.ModelForm):
    class Meta:
        model = Ogrenci
        fields = ['TC', 'Adi','Soyadi']  # Kullanmak istediğiniz alanları buraya ekleyin

from django.shortcuts import render

def ogrenci_kaydet(request):
    if request.method == 'POST':
        form = OgrenciForm(request.POST)
        if form.is_valid():
            # Form verileri işleme
            form.save()  # Veritabanına kaydetme
            return redirect('listele') #url name

    else:
        form = OgrenciForm()
    return render(request, 'ogrenciekle1.html', {'form': form})

from django.shortcuts import get_object_or_404, redirect

def guncelle(request, id):
    ogrenci = get_object_or_404(Ogrenci, id=id)
    # ogrenci = Ogrenci.objects.get(id=id)
    if request.method == 'POST':
        form = OgrenciForm(request.POST, instance=ogrenci)
        if form.is_valid():
            # Form verileri işleme
            form.save()  # Veritabanına kaydetme
            return redirect('listele')
    else:
        form = OgrenciForm(instance=ogrenci)
    return render(request, 'ogrenciekle1.html', {'form': form})

# def guncelle(request, id):
#     ogrenci = get_object_or_404(Ogrenci, id=id)  # İlgili Ogrenci nesnesini getiriyoruz

#     if request.method == 'POST':
#         form = OgrenciForm(request.POST, instance=ogrenci)
#         if form.is_valid():
#             form.save()  # Güncellenmiş veriyi veritabanına kaydetme
#     else:
#         form = OgrenciForm(instance=ogrenci)  # Güncelleme formu, mevcut veriyle doldurulur

#     return render(request, 'ogrenciekle1.html', {'form': form})