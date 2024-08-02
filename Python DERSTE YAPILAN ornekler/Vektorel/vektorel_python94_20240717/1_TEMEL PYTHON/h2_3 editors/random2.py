import random, turtle
# # print(random.random()) # 0 ile 1 arası bir sayı
# print(random.randint(1,100))

# meyveler= ["elma","armut","nar","muz"]
# print(random.choice(meyveler))
renk = ["red","green","blue"]
for b in range (10):
    turtle.up()
    turtle.goto(random.randint(-200,200),random.randint(-200,200))
    turtle.down()
    buyukluk = random.randint(1,200)
    turtle.color(renk[random.randint(0,2)])
    for a in range(4):
        turtle.forward(buyukluk)
        turtle.right(90)

input()