def duzListele():

    print("\nREHBER KAYIT LİSTESİ")
    print("====================")
    dosya = open("rehber.txt","r")
    okunan = dosya.read()
    print(okunan)

def siraliListele():
    print("\nREHBER SIRALI KAYIT LİSTESİ")
    print("===========================")
    dosya = open("rehber.txt","r")
    okunan = dosya.readlines()
    for a in okunan:
        print(a.strip())
    
    
