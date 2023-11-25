def tahtaOlustur(boyutT,bosKarakter,yerX,yerY,karakterYilan):
    tahta = []
    for a in range(boyutT):
        sira = []
        for b in range(boyutT):
            if a==yerX and b==yerY : sira.append(karakterYilan)
            else: sira.append(bosKarakter)
        tahta.append(sira)

    Satir =""
    for a in range(boyutT):
        for b in range(boyutT):
            Satir += tahta[a][b]
        print (Satir)
        Satir =""
    print("\n")
import random
boyut = 10
karakter = "░"
x = random.randint(0,boyut)
y = random.randint(0,boyut)
yilanKarakteri = "©"
tahtaOlustur(boyut,karakter,x,y,yilanKarakteri)

# Basılan tuşları algılama
# pip install keyboard
import keyboard

def on_key_event(event):
    global x
    global y
    if event.name == 'up' or event.name == 'down' or event.name == 'left' or event.name == 'right':
        # print(f"Girilen yön tuşu: {event.name}")
        if event.name == "right": 
            y+=1
        if event.name == "left": 
            y-=1
        if event.name == "up": 
            x-=1
        if event.name == "down": 
            x+=1
        if x>boyut : x=1
        if x<0: x=boyut
        if y>boyut : y=1
        if y<0 : y = boyut
        tahtaOlustur(boyut,karakter,x,y,yilanKarakteri)

keyboard.on_release(on_key_event)

keyboard.wait('esc')  # Programın çalışmasını sonlandırmak için "esc" tuşuna basın
