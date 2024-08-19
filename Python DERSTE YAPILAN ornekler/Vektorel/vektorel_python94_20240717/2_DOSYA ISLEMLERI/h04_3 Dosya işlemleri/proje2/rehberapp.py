import keyboard
dosyaadi = "rehber.txt"
aktifMenu = 1
def menu():  
    global aktifMenu  
    print("\033[1;32;40m")
    #print("╔"+"═"*20+"╗")
    print("╔═════════════════════╗")
    print("║\033[1;31;40m   REHBER APP  \033[1;32;40m  ║")
    print("║                     ║")
    print("║ >1-İsim ekle   <    ║" if aktifMenu==1 else "║  1-İsim ekle        ║") 
    print("║ >2-Listele     <    ║" if aktifMenu==2 else "║  2-Listele          ║") 
    print("║ >3-Sil         <    ║" if aktifMenu==3 else "║  3-Sil              ║") 
    print("║                     ║")
    print("║    Seçimiz nedir?   ║")
    print("╚═════════════════════╝")
    # 201 ╔ # 205 ═ # 187 ╗ # 186 ║ # 200 ╚ # 188 ╝
    
    def on_key_event(event):
            global aktifMenu
        # if event.name == 'up' or event.name == 'down' or event.name == 'left' or event.name == 'right':
            # print(f"Girilen yön tuşu: {event.name}")
            if event.name == "up" : aktifMenu -=1
            if event.name == "down" : aktifMenu +=1
            if event.name == "enter" : 
                if aktifMenu == 1: kisiEkle()

            if aktifMenu>3 : aktifMenu=1
            if aktifMenu<0 : aktifMenu=3
            menu()

    keyboard.on_release(on_key_event)

    keyboard.wait('esc')  # Programın çalışmasını sonlandırmak için "esc" tuşuna basın    
    
    
    
    
    
    
    # tus = input(f"{aktifMenu} A=Aşağı/Y=Yukarı/S=SEç").upper()
    # if tus == "A" : aktifMenu +=1
    # if tus == "Y" : aktifMenu -=1
    # if tus == "S" : 
    #     if aktifMenu == 1: kisiEkle()

    # if aktifMenu>3 : aktifMenu=1
    # if aktifMenu<1 : aktifMenu=3
    # menu()

def kisiEkle():
    d = open(dosyaadi, "a", encoding="utf-8")
    ad = input("Kaydedilecek kişi adı:")
    no = input("Kaydedilecek kişi adı:")
    d.write(f"Adı:{ad}\tNumarası:{no}\n")
    d.close()

menu()