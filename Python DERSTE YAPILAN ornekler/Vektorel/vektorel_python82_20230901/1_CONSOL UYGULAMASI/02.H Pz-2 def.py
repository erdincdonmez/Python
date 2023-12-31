import turtle as t

def kareciz(xxr):
    for k in range(4):
        t.forward(xxr)
        t.right(90)

def sekilciz(buy,ken):
    for k in range(ken):
        t.forward(buy)
        t.right(360/ken)

# buyukluk = int(input("Büyüklük ne olsun: ")) 
# tekrar   = int(input("kaç tane olsun   : ")) 

for a in range (50,350,30):
    # print(a)
    kareciz(a)
# sekilciz(100,6)

input()