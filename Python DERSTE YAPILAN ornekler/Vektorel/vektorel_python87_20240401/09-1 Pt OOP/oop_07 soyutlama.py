# @abstractmethod abc modülünde bulunur.
from abc import ABC, abstractmethod

class Hayvan(ABC):
    def __init__(self):
        print("\nHayvan oluştu")

    @abstractmethod
    def sesCikar(self): pass

    @abstractmethod
    def hareketKabiliyeti(self): pass

class Kus(Hayvan):
    def __init__(self):
        print("\nKuş oluştu")

    def sesCikar(self):
        print("Kuşlar Cik cik sesi çıkarır")
   
    def hareketKabiliyeti(self):
        print("Kuşlar uçar")

class Ari(Hayvan):
    def sesCikar(self):
        print("Arılar vız vız sesi çıkarır")

    def hareketKabiliyeti(self):
        print("Arılar uçar")
h1 = Kus()
h1.sesCikar()
h2 = Ari()
h2.sesCikar()
h2.hareketKabiliyeti()
