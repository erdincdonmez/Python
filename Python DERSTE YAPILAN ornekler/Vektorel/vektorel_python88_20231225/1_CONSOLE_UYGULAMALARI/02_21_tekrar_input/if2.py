print("Futbol takımına notu 85 üzeri erkek öğrenciler katılabilir.")
puan = int(input ("Matematik puanın kaç? "))
c = input ("Cinsiyetin nedir? ")
if puan < 0 or puan > 100 :
    print("Yanlış giriş")
else :
    if puan > 85 : print ("Puanın çok güzel")
    elif puan > 70 : print ("Puanın iyi")
    elif puan > 50 : print ("Geçmişsin")
    else : print ("Kalmışsin dostum.")

if puan>85 and (c=="erkek" or c=="Erkek"):
    print("Futbol takımına girebilirsin")
else : print("Takıma giremezsin")

