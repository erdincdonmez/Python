try:
    okunan = open("deneme1.txt","r")
    print(okunan.read())
    okunan.close()
except:
    print("Bir hata oluştu.")
