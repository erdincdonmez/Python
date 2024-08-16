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
    tus = input(f"{aktifMenu} A=Aşağı/Y=Yukarı/S=SEç").upper()
    if tus == "A" : aktifMenu +=1
    if tus == "Y" : aktifMenu -=1
    if tus == "S" : 
        if aktifMenu == 1: kisiEkle()
        if aktifMenu == 2: listele()

    if aktifMenu>3 : aktifMenu=1
    if aktifMenu<1 : aktifMenu=3
    menu()

def kisiEkle():
    d = open(dosyaadi, "a", encoding="utf-8")
    ad = input("Kaydedilecek kişi adı: ")
    no = input("Kaydedilecek numarası: ")
    # d.write(f"Adı:{ad}\tNumarası:{no}\n")
    d.write(str({"adi":ad,"num":no})+",")
    d.close()

def listele():
    ddd = open(dosyaadi,encoding="utf-8")
    print("\n\n KİŞİLER LİSTESİ:\n===============")
    # print(ddd.read())
    okunan = ddd.read()
    # okunan = ddd.readlines()
    # okunan.split(",") xxx
    print(okunan)

    import ast
    cevirilen = ast.literal_eval(okunan)

    for b in cevirilen:
        # print(b)
        # print(b["adi"])
        if b["adi"]=="Ozan CAN": print("ozanı bulduk")

def degistir():
    ddd = open(dosyaadi,encoding="utf-8")
    print("\n\n KİŞİLER LİSTESİ:\n===============")
    # print(ddd.read())
    okunan = ddd.read()
    # okunan = ddd.readlines()
    # okunan.split(",") xxx
    print(okunan)

    import ast
    cevirilen = ast.literal_eval(okunan)
    yeniveriler={}
    ddd = open(dosyaadi,"w",encoding="utf-8")
    for b in cevirilen:
        # print(b)
        # print(b["adi"])
        if b["adi"]=="Beste VAROL": 
            b["adi"]="Beste"
        ddd.write(str({"adi":b['adi'],"num":b["num"]})+",")
degistir()