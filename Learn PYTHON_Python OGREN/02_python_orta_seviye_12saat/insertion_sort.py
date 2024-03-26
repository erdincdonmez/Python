# insertion sort
dizi = [22,27,16,2,18,6]
for i in range(1, len(dizi)):
  deger = dizi[i]
  j = i-1
  while j >=0 and deger<dizi[j] :
    dizi[j+1] = dizi[j]
    j -= 1
    dizi[j+1] = deger
print(dizi)

"""
- Yukarı verilen dizinin sort türüne göre aşamalarını yazınız.

[22,27,16, 2,18, 6] 
[ 2,22,27,16,18, 6] 
[ 2, 6,22,27,16,18] 
[ 2, 6,16,22,27,18] 
[ 2, 6,16,18,22,27]
[ 2, 6,16,18,22,27]
[ 2, 6,16,18,22,27]


- Big-O gösterimini yazınız.

n^2 = 36


- Time Complexity:

En iyi durum  : O(n)   (Best case: Dizinin sıralı olması durumu)
En kötü durum : O(n^2) (Worst case: Aradığımız sayının sonda olması)
Ortalama      : O(n^2) (Average case: Aradığımız sayının ortada olması)

- Dizi sıralandıktan sonra 18 sayısı hangi case kapsamına girer? 

Ortalama (Avarege)
"""