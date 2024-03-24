# ROI = Region of Interest
import cv2

img1 = cv2.imread('images/square1.jpg')
# roi = img1[y1:y2, x1:x2]
# parca = img1[200:400, 200:400] # sol göz
parca = img1[400:520, 400:650] # burun
img1[330:450, 400:650] = parca

cv2.imshow('parça',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()