import random
import turtle

t = turtle.Turtle()
# Kodunuzu buraya yazınız
while True:
    uzunluk = int(input("Çizginin uzunluğu ne kadar olmalı:"))
    if uzunluk == 0:
        break
    aci = random.randint(1, 360)
    t.left(aci)
    t.forward(uzunluk)
