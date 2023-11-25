def sayitahminoyunu():
    import random
    tahmin = input("Yazı mı Tura mı?").lower()

    yt = random.randint(1,2)
    #print(yt)

    if yt == 1 : atilan = "Yazı"
    else: atilan = "Tura"

    print("Parayı attım")
    print("Gelen: ",atilan)
    if atilan.lower() == tahmin.lower() : print("Kazandın")
    else : print("Olmadı")
    cevap = input("Tekrar oynamak ister misin? (e/h)")
    if cevap.lower() == "e" : sayitahminoyunu()
    else: print("İyi günler.\nAna menuye dönülüyor.")

# sayitahminoyunu()