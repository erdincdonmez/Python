import random
sorular = []
cevaplar = []

def menu():
    print("BİLGİ YAŞIMASI")
    print("==============")
    print("1-Soru girme")
    print("2-Yarışma")
    secim=input("Seçiminiz: ")
    if secim == "1" : soruGir()
    if secim == "2" : yarisma()
    
def soruGir():
    #kacSoru = int(input("Kaç soru olacak"))
    soru=""
    while soru.lower()!="bitti":    
        soru = input("Soru giriniz: ")
        sorular.insert(1,soru)
        if soru == "bitti": break
        cevap = input("Cevabını giriniz: ")
        cevaplar.insert(1,cevap)
        
        print ("\nSORULAR ")
        print ("=======")
        for s in sorular:
            print(sorular.index(s)+1,"=>",s," Cevabı:",cevaplar[sorular.index(s)])
    menu()

def yarisma():
    soruNo = random.randint(0,len(sorular))
    cevap = input(sorular[soruNo])
    if cevap == cevaplar[soruNo] :
        print("bildin")
    else:
        print("bilemedin")
    menu()
    

menu()




