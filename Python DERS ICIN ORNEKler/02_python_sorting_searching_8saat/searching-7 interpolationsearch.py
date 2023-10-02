def InterpolationSearch(arananYer, aranan):
    basi = 0
    sonu = (len(arananYer) - 1)
    while basi <= sonu and aranan >= arananYer[basi] and aranan <= arananYer[sonu]:
        yeri = basi + int(((float(sonu - basi) / ( arananYer[sonu] - arananYer[basi])) * ( aranan - arananYer[basi])))
        if arananYer[yeri] == aranan:
            return yeri
        if arananYer[yeri] < aranan:
            basi = yeri + 1;
        else:
            sonu = yeri - 1;
    return -1
print(InterpolationSearch([1,2,3,4,5,6,7,8], 9))
