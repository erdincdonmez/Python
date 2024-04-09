# cv2'de eventlar
import cv2

cv2komutlari = dir(cv2)
# print(cv2komutlari)
sayac = a = 0

for sira, xx in enumerate(cv2komutlari, start=1):
    if 'EVENT' in xx: a +=1 ; print(f"{a}-{sira} {xx}")