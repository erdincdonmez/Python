def FibonacciileAra(AranacakYer, aranan):
    fibS_onceki_2 = 0
    fibS_onceki_1 = 1
    fibS = fibS_onceki_1 + fibS_onceki_2
    while (fibS < len(AranacakYer)):
        fibS_onceki_2 = fibS_onceki_1
        fibS_onceki_1 = fibS
        fibS = fibS_onceki_1 + fibS_onceki_2
    yer = -1;
    while (fibS > 1):
        i = min(yer + fibS_onceki_2, (len(AranacakYer)-1))
        if (AranacakYer[i] < aranan):
            fibS = fibS_onceki_1
            fibS_onceki_1 = fibS_onceki_2
            fibS_onceki_2 = fibS - fibS_onceki_1
            yer = i
        elif (AranacakYer[i] > aranan):
            fibS = fibS_onceki_2
            fibS_onceki_1 = fibS_onceki_1 - fibS_onceki_2
            fibS_onceki_2 = fibS - fibS_onceki_1
        else :
            return i
    if(fibS_onceki_1 and yer < (len(AranacakYer)-1) and AranacakYer[yer+1] == aranan):
        return yer+1;
    return -1
print(FibonacciileAra([1,2,3,4,5,6,7,8,9,10,11], 1))
