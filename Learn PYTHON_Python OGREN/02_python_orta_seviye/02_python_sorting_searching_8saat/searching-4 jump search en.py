import math

def AtlayarakAra (ArananilacakYer, aranan):
    elemansayisi = len(ArananilacakYer)
    atlamamiktari = int(math.sqrt(elemansayisi))
    basi, sonu = 0, 0
    while basi < elemansayisi and ArananilacakYer[basi] <= aranan:
        sonu = min(elemansayisi - 1, basi + atlamamiktari)
        if ArananilacakYer[basi] <= aranan and ArananilacakYer[sonu] >= aranan:
            break
        basi += atlamamiktari;
    if basi >= elemansayisi or ArananilacakYer[basi] > aranan:
        return -1
    sonu = min(elemansayisi - 1, sonu)
    i = basi
    while i <= sonu and ArananilacakYer[i] <= aranan:
        if ArananilacakYer[i] == aranan:
            return i
        i += 1
    return -1
print(AtlayarakAra([1,2,3,4,5,6,7,8,9], 9))
