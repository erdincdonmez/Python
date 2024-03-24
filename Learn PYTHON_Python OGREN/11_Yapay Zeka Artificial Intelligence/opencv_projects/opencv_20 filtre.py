# filtre
import cv2

img1 = cv2.imread('images/square1.jpg')

# img1[y1:y2, x1:x2,BGR indisi] = yenideger_max_255 

# img1[:,:,0] = 0 # Blue değerlerini 0 yap
# img1[:,:,1] = 0 # Green değerlerini 0 yap
# img1[:,:,2] = 0 # Red değerlerini 0 yap

# img1[:,:,0] = 255 # Blue değerlerini 255 yap
img1[:,:,1] = 255 # Green değerlerini 255 yap
# img1[:,:,2] = 255 # Red değerlerini 255 yap

cv2.imshow('filtreli',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()