from django.db import models

class Ogrenci(models.Model):
    TC = models.CharField(max_length=11)
    Adi = models.CharField(max_length=30)
    Soyadi = models.CharField(max_length=20)
    Telefon = models.IntegerField(null=True)

def __str__(self):
    return f"{self.Adi} {self.Soyadi}"

class Veli (models.Model):
    TC = models.CharField(max_length=11)
    AdiSoyadi = models.CharField(max_length=50)

class Ogretmen (models.Model):
    TC = models.CharField(max_length=11)
    AdiSoyadi = models.CharField(max_length=50)
    Bransi = models.CharField(max_length=30)
    


