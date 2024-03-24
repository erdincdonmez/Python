import turtlex as turtle
import random

t = turtle.Turtle()
t.up()
t.goto(-100, 100)
t.down()
t.speed(0)

# yarış pisti
for i in range(15):
    t.write(i)
    t.right(90)
    t.forward(200)
    t.left(180)
    t.forward(200)
    t.right(90)
    t.forward(20)

# kablumbağaları oluşturma
birinci = turtle.Turtle()
birinci.shape("turtle")
birinci.color("red")
birinci.up()
birinci.goto(-120, 70)
birinci.down()

ikinci = turtle.Turtle()
ikinci.shape("turtle")
ikinci.color("blue")
ikinci.up()
ikinci.goto(-120, 40)
ikinci.down()

ucuncu = turtle.Turtle()
ucuncu.shape("turtle")
ucuncu.color("yellow")
ucuncu.up()
ucuncu.goto(-120, 10)
ucuncu.down()

# taraftarlar
x = random.randint(1, 10)
for i in range(x):
    taraftar = turtle.Turtle()
    k = random.randint(0, 255) / 255.0  # Renk değerlerini normalize et
    y = random.randint(0, 255) / 255.0
    m = random.randint(0, 255) / 255.0
    taraftar.shape("turtle")
    taraftar.color(k, y, m)
    taraftar.up()
    taraftar.goto(-90 + 25 * i, -120)
    taraftar.down()
    taraftar.left(90)

x_birinci = 0
x_ikinci = 0
x_ucuncu = 0

kazanan = input("Hangi kablumbağa kazanacak:")
yazi = turtle.Turtle()
yazi.up()
yazi.goto(-120, 120)
yazi.write(kazanan + " kablumbağanın kazanacağını düşünüyorsunuz ")

while True:
    if x_birinci > 305 or x_ikinci > 305 or x_ucuncu > 305:
        break

    birinci_adim = random.randint(1, 5)
    x_birinci = x_birinci + birinci_adim
    birinci.forward(birinci_adim)

    ikinci_adim = random.randint(1, 5)
    x_ikinci = x_ikinci + ikinci_adim
    ikinci.forward(ikinci_adim)

    ucuncu_adim = random.randint(1, 5)
    x_ucuncu = x_ucuncu + ucuncu_adim
    ucuncu.forward(ucuncu_adim)

if x_birinci > 305:
    t.write("Kırmızı Kazandı!")
elif x_ikinci > 305:
    t.write("Mavi Kazandı!")
elif x_ucuncu > 305:
    t.write("Sarı Kazandı!")

input()
