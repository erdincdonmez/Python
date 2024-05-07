# boş resim oluşturma
import cv2
import numpy as np

r1 = cv2.imread('resimler/bayrak2.jpg')
print(r1)

cv2.imshow("Olusan resim", r1)

cv2.waitKey(0)
 
cv2.destroyAllWindows()