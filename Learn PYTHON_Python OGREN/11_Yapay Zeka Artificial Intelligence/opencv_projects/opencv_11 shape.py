# Temel resim özellikleri - shape
import cv2
img1 = cv2.imread('images/square1.jpg')
img2 = cv2.imread('images/square1.jpg',0)

print(img1.shape) # 3 RGB ifadesidir
print(img2.shape)

genislik, yukseklik, renk = img1.shape

print(f"Resmin genisliği:{genislik}, yüksekliği:{yukseklik}, rengi:{renk}")

# shape
# size
# datatype
# ROI
# renk filtresi