# cv2'de 2400 civarı fonksiyon
import cv2

cv2komutlari = dir(cv2)
print(cv2komutlari)
sayac = 0

for sira, xx in enumerate(cv2komutlari, start=1):
    print(f"{sira}. {xx}")