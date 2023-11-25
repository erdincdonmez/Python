def saydir():
    bas = int(input("Kaçtan başlayayım  : "))
    son = int(input("Kaça kadar sayayım : "))
    art = int(input("Kaçar kaçar sayayım: "))
    say(bas,son,art)

def say(x,y,z):
    for abc in range(x,y+1,z):
        print (abc)

# 9 numaralı görevi yap.
# Kaçtan kaça kadar,kaçar kaçar
# sayacağını sor ve saydır.
