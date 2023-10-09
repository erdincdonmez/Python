kelime = "vektörel"

for a in range(len(kelime)+1):
    yazilacak = kelime[:a]
    yazilacakTersi = ""
    for b in range(len(yazilacak)-1,0,-1):
        yazilacakTersi += yazilacak[b]
    print(yazilacak+ " "*(len(kelime)-a)*2, yazilacakTersi)
