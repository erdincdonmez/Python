# a = 0
# def selamla(x):
#     global a
#     # a=0
#     a += 1
#     print("merhaba", x)

#     if a != 10 : selamla(a)

# selamla(0)

# Faktöriyel hesapla
fhs = 4 # Faktöriyeli Hes.Say.
sonuc = 1
def faktoriyel(xx):
    global sonuc
   
    sonuc *= xx
    print("Sayi:",xx)
   
    xx -= 1
    if xx > 1: faktoriyel(xx)

faktoriyel(fhs)
print(f"{fhs} faktöriyeli: ",sonuc)

