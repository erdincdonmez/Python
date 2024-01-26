import turtle as t
t.speed(100)
def kare(x):
    if x < 50 : return x
    else:
        for i in range (4):
            t.forward(x)
            t.right(90)
        return kare(x-10)

aaa = int (input("Karenin uzun kenarı ne kadar?"))
kare(aaa)
input()