# Resim açma
import cv2
img = cv2.imread('images/square1.jpg')
cv2.imshow('Deneme',img)
# cv2.waitKey(0) # herhangi bir tuşa basılana kadar bekle
cv2.waitKey(3000) # 3 saniye bekle
cv2.destroyAllWindows()