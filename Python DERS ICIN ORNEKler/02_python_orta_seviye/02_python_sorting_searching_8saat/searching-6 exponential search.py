def BinarySearch(lys, val):
    first = 0
    last = len(lys)-1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if lys[mid] == val:
            index = mid
        else:
            if val<lys[mid]:
                last = mid -1
            else:
                first = mid +1
    return index
def UsAlarakAra(AranacakYer, aranan):
    if AranacakYer[0] == aranan:
        return 0
    yeri = 1
    while yeri < len(AranacakYer) and AranacakYer[yeri] <= aranan:
        yeri = yeri * 2
    return BinarySearch( arr[:min(yeri, len(AranacakYer))], aranan)

print(UsAlarakAra([1,2,3,4,5,6,7,8],3))
