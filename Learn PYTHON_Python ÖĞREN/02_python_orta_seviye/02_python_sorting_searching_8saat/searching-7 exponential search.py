def bolerekAra( aranacakYer, basi, sonu, aranan):
    if sonu >= basi:
        orta = basi + ( sonu-basi ) // 2
        if aranacakYer[orta] == aranan: # If the element is present at
            return orta # the middle itself
        if aranacakYer[orta] > aranan:# If the element is smaller than orta,
            return bolerekAra(aranacakYer, basi, orta - 1, aranan)# then it can only be present in theleft subaranacakYeray
        return bolerekAra(aranacakYer, orta + 1, sonu, aranan)# Else he element can only be present in the right
    return -1 # We reach here if the element is not present
# Returns the position of first occurrence of aranan in aranacakYeray
def ustalarakAra(aranacakYer, elemanSayisi, aranan):
    if aranacakYer[0] == aranan: # IF aranan is present at first
        return 0 # location itself
    i = 1
    while i < elemanSayisi and aranacakYer[i] <= aranan: # Find range for binary search
        i = i * 2 # j by repeated doubling    
    return bolerekAra( aranacakYer, i // 2, min(i, elemanSayisi-1), aranan)# Call binary search for the found range
aranacakYer = [2, 3, 4, 10, 40] # Driver Code
elemanSayisi = len(aranacakYer)
aranan = 22
yeri = ustalarakAra(aranacakYer, elemanSayisi, aranan)
if yeri == -1: print (aranan,"elemanı",aranacakYer,"dizisinde bulunamadı") 
else: print ("Aradığınız elemanın yeri %d" %(yeri))
 
