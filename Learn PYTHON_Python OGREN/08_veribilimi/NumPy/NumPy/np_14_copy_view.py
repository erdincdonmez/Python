# COPY ve VIEW
import numpy as np

dz = np.array([1, 2, 3, 4, 5])
aa = dz.copy() # Benzeri bir kopyasını oluşturma
bb = dz.view() # Benzeri bir referans oluşturma

print("\norjinal dz dizisi  :",dz) # orjinal dizi
print("copy ile aa dizisi :",aa) 
print("view ile bb dizisi :",bb) 

dz[0] = 77 # orjinal arrayi değiştirme
print("\norjinaldeki dz[0]=77 değişikliği sonrası dz :",dz) # orjinaldeki değişik sonrası
print("orjinaldeki dz[0]=77 değişikliği sonrası aa :",aa) # orjinaldeki değişik sonrası
print("orjinaldeki dz[0]=77 değişikliği sonrası bb :",bb) # orjinaldeki değişik sonrası

aa[2] = 88 # dz kopyası aa dizisini değiştirme
print("\ncopy'deki aa[2]=88 değişikliği sonrası dz :",dz) # copy değişikliği sonrası
print("copy'deki aa[2]=88 değişikliği sonrası aa :",aa) # copy değişikliği sonrası
print("copy'deki aa[2]=88 değişikliği sonrası bb :",bb) # copy değişikliği sonrası

bb[4] = 99 # dz viewi aa dizisini değiştirme
print("\nview'deki bb[4]=99 değişikliği sonrası dz :",dz) # view değişikliği sonrası
print("view'deki bb[4]=99 değişikliği sonrası aa :",aa) # view değişikliği sonrası
print("view'deki bb[4]=99 değişikliği sonrası bb :",bb) # view değişikliği sonrası

print(aa.base)
print(bb.base)