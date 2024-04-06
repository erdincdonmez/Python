tamam = False
while tamam==False:
    try:
        veri = input("Puan girin:")        
        print("Puan: ",veri)
        print(type(veri))
        print(int(veri))
        tamam = True
    except:
        print("Sayısal bir veri girin.")
    
