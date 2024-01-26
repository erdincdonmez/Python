a = 5
fktryl = 1
def faktoriyel(x):
    global fktryl 

    if x<2 : return fktryl
    else:
        # global fktryl 
        fktryl *= x
        return faktoriyel(x)

print (faktoriyel(a))