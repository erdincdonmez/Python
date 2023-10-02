
konu = "SANAL SOHEBETE HOŞ GELDİNİZ."
print(konu)
print("="*len(konu))

ad = input("Adınız nedir?")
print ("Merhaba",ad)
cevap = input("Benimle sohbet etmek ister misin?(evet/hayır) : ")
if cevap == "evet":
    print("Benimle sohbet etmek istediğine sevindim",ad)
    yil = int(input("hangi yılda doğdun?"))
    if 2021-yil > 60 :
        print ("Torunun var mı?")
    if 2021-yil >6 and 2021-yil<20 :
        print ("Hangi okula gidiyorsun")
elif cevap == "hayır" :
    print ("Peki görüşürüz")
else:
    print ("dediğini anlayamadım")

