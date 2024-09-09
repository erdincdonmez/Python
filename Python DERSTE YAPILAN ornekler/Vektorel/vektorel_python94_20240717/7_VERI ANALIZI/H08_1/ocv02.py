# Ör-2: Resim açma
import cv2
# img = cv2.imread('images/square1.jpg')
img = cv2.imread('turk_bayragi.png')
cv2.imshow('Deneme',img)
print (img)
print ("\n\n",img[45][60])
# cv2.waitKey(3000) # 3 saniye bekle
cv2.waitKey(0) 
cv2.destroyAllWindows() # pencereleri kapa
