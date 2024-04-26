# dictionary türünde kwargs
def yaz(**xx):
    print(xx)
    print("Soyadı :" + xx["soyad"])

yaz(ad = "Eren", soyad = "AKIN")