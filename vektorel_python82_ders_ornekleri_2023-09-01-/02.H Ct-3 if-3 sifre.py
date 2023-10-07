print("FBI GİZLİ PROGRAMI")
print("==================")
ka = input("Kullanıcı adı: ")
sf = input("Şifre        : ")

dka = "admin"
dsf = "123"

if ka==dka and sf==dsf:
    print("Giriş yapıldı.")
    secim = input("Ne şekli çizeyim?")
    if secim =="kare" or secim=="Kare" or "KARE":
        import turtle
        for a in range (4):
            turtle.forward(100)
            turtle.right(90)
        input()
elif ka==dka and sf!=dsf:
    print("Şifre yanlış")
elif ka!=dka and sf==dsf:
    print("Kullanıcı adı yanlış")
elif ka!=dka and sf!=dsf:
    print("İkisi de yanlış")
else: print("Sistem hatası")