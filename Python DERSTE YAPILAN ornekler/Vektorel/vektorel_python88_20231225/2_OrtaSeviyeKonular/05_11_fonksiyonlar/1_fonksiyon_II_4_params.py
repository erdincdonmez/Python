def birlestir(**xxx):

    print("Gelen değer:",xxx) 
    for (aa,bb) in xxx:
        print(aa,bb)
    # print(xxx["adi"])
    return xxx["soyadi"] +" "+ xxx["adi"]


print("Toplam:",birlestir(adi="Mustafa",soyadi="Oğuzalp"))
