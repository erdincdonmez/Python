# Dizilerden [başlangıç:bitis:atlamamiktarı]
# belirterek parça alabiliriz.
# Başlangıç dahil, bitiş dahil değil 
# 1:4 demek 1,2,3 indisliler demek
import numpy as np
arr = np.array([1,2,3,4,5,6,7])
print("arr :", arr) # arr dizisi
print("arr[1:5] :", arr[1:5]) # 1-5 arası
xx = np.array([1,2,3,4,5,6,7,8,9])
print("xx :", xx) # xx dizisi
print("xx[0:9:2] :", xx[0:9:2]) # 0-9 arası ikişer atlayarak
print("xx[4:] :", xx[4:]) # 4'ten itibaren
print("xx[:4] :", xx[:4]) # 4'e kadar
print("xx[:] :", xx[:]) # hepsi
print("xx[-3:-1] :", xx[-3:-1]) # negatif index
print("xx[::2] :", xx[::2]) # hepsinden ikişer atlayarak

# iki boyutlu dizilerde (2D) dizi bölme
arr2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print("arr2[1, 1:4] :", arr2[1, 1:4]) # indisi 1 olan elemandan 1-4 arasını al.
print("arr2[0:2, 2] :", arr2[0:2, 2])  # indisi 0 ve 1 olanların 2.indislerini al.
print("arr2[0:2, 1:4] :", arr2[0:2, 1:4]) # indisi 0 ve 1 olanların 1-4 arası olanlarını al.