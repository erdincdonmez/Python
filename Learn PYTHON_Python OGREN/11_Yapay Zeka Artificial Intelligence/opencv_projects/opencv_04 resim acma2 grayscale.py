# Resim açma, gritonlu
import cv2
# img = cv2.imread('images/square1.jpg',cv2.IMREAD_GRAYSCALE)
img = cv2.imread('images/square1.jpg',0)
cv2.imshow('Deneme',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
