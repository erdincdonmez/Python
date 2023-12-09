dosya = open("deneme.txt","a")
ad1 =    input("Ad    : ")
soyad1 = input("Soyad : ")
numara1= input("Numara: ")
yazilacak = ad1 +"|"+ soyad1 +"|"+ numara1 +"\n"
yaz = [ad1,soyad1,numara1]
yazd = {"ad":ad1,"soyad":soyad1,"numara":numara1}
print(type(yazd))
dosya.write(str(yazd)+"\n")
dosya.write("\n")
dosya.close()