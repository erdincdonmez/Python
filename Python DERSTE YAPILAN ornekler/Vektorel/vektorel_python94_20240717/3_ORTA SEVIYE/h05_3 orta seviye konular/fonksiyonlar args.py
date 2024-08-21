# def topla(a):
#     print(a)
#     toplam = 0
#     for x in a:
#         toplam+=x
#     print("Toplam: ",toplam)      
# topla([3,4,2,5,6])

def topla(*a):
    print(a)
    toplam = 0
    for x in a:
        toplam+=x

    print("Toplam: ",toplam)
        
topla(3,4,2,5,6)
