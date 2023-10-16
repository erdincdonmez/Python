#Faktöriyel bir sayıya kadar olan sayıların çarpımıdır.
def faktoriyel(x):
    if x == 1:
        return 1
    else:
        return (x * faktoriyel(x-1))
sayi = 6
print(sayi, "sayısının faktöriyeli", faktoriyel(sayi))
