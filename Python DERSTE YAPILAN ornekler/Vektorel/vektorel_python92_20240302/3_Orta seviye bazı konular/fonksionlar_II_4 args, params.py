# args
yy = [55,2,41,62]
def topla(*xx):

    print(xx)
    # print(yy)
    # yy.pop()
    # print(yy)
    topla = 0
    for a in xx:
        # print(a,end=" ")
        print(a)
        topla += a
    print(topla)
    print(xx[3])
    
topla(55,2,41,62)
