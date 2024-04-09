import cv2
# OpenCV sürümünü al
opencv_versionu = cv2.__version__
# Sürümü ekrana yazdır
print("OpenCV sürümü:", opencv_versionu)

cv2komutlari = dir(cv2)
print(cv2komutlari)
sayac = 0

for sira, xx in enumerate(cv2komutlari, start=1):
    print(f"{sira}. {xx}")