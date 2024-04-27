class KekKalibi():
    def __init__(self, *args):
        for a in args: print(a,end=",")
        self.icerik = args
        print(" içeren bir kek üretildi.")

    def kekBilgisiGoster(self):
        print("Kek içeriği: ",self.icerik)

kekler = []
kekTuru = " "
while kekTuru!="":
    kekTuru = input ("Kekin neyli olsun?")
    kek = KekKalibi(kekTuru)
    kekler.append(kek)

for a in kekler:
    print(a.kekBilgisiGoster())
# print(kek1.icerik)
# print(kek1.kekBilgisiGoster())
#  Son satırda none niye yazıyor?