# ROI = Region of Interest
import cv2

img1 = cv2.imread('images/square1.jpg')
# roi = img1[y1:y2, x1:x2]
roi = img1[200:400, 200:400]

cv2.imshow('parça',roi)
cv2.waitKey(0)
cv2.destroyAllWindows()