# Temel resim özellikleri - datatype
import cv2
img1 = cv2.imread('images/square1.jpg')
img2 = cv2.imread('images/square1.jpg',0)

print(img1.dtype)
print(img2.dtype)

# ROI
# renk filtresi