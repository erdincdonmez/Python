# Temel resim işlemleri - itemset
import cv2

img1 = cv2.imread('images/ornekresim01_150x100.png')

for a in range(50,80):
    for b in range(50,80):
        img1.itemset((a,b,0),0) # 1 Blue max=255
        img1.itemset((a,b,1),0) # 2 Green max=255
        img1.itemset((a,b,2),255) # 3 Red max=255

cv2.imshow('değişiklik',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()