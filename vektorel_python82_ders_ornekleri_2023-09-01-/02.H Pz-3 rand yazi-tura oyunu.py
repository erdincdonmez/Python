import random

def yazituraat():
    uretilen = random.randint(1,2)
    atilan = ""
    if uretilen == 1: atilan="yazı"
    if uretilen == 2: atilan="tura"
    return atilan

yt = yazituraat()

tahmin = input("yazı mı tura mı?")

if tahmin == yt: print("bildin")
else: print ("bilemedin")
