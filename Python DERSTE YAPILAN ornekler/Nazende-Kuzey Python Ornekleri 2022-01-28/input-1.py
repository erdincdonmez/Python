print("BENİMLE SOHBET ETMEK İSTER MİSİN")
print("================================\n")

#input komutun bu şekilde kullanabiliriz.
#print("Adınızı giriniz:")
#a = input()

#Bu da inputun ikinci kullanım şekli
a = input("Adınızı giriniz:")
print("Demek adın",a,". Adın güzelmiş",a)

#soru = "Benimle sohbet etmek ister misin?"+str(a)
cevap = input("Benimle sohbet etmek ister misin "+str(a)+"? (evet/hayır) :")
 
if cevap=="evet" :
    print ("Benimle sohbet etmek istediğine sevindim.")
    dy = int(input ("Kaç yılında doğdun?"))
    print ("Demek",2021-dy,"yaşıdasın",a)
    meslek = input("Ne iş yapıyorsun?")
    if meslek == "öğrenci" :
        print ("Derslerin iyidir umarım.")
    if meslek == "öğretmen" :
        print("Hıımm öğretmenlik çok güzel bir meslek")
        brans = input("Branşınız ne?")
        print (brans," öğretmenliği güzel.")        
if cevap=="hayır" :
    print ("Peki o zaman görüşürüz.")
else :
    print ("Seni anlayamadım...")
