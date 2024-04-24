# @abstractmethod abc modülünde bulunur.
from abc import ABC, abstractmethod

class Calisan(ABC):
    def __init__(self):
        print("\nSınıf oluştu")

    @abstractmethod
    def yemekMenuYazdir(self): pass

class Ogretmen(Calisan):
    def __init__(self): print("\nSınıf oluştu")
    def yemekMenuYazdir(self):
        print("Çorba, Yemek + İçecek")

class Personel(Calisan):    
    def __init__(self): print("\nSınıf oluştu")
    def yemekMenuYazdir(self):
        print("Çorba, Yemek")

# calisan = Calisan()
calisan1 = Personel()
calisan2 = Ogretmen()

calisan1.yemekMenuYazdir()
calisan2.yemekMenuYazdir()