a = 5
a = 6
def topla():
    a = 7 # 
    print("İçte:",a)

def carp():
    global a
    a = 8
    print("Çarpta:",a)

topla()
carp()
print("Dışta:",a)
