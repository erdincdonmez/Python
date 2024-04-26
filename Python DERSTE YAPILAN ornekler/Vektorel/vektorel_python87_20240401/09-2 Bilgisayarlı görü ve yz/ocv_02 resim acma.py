# pip install opencv-python
# import cv2
# print(cv2.__version__)

import cv2
img = cv2.imread('images/bayrak1.png')
cv2.imshow('Deneme',img)
cv2.waitKey(3000) # 3 saniye bekle
cv2.destroyAllWindows() # pencereleri kapa