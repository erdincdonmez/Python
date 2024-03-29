# pyrUp
import cv2
import numpy as np
r1 = cv2.imread("images/top1.jpg")
  
for a in range(5):
    r1 = cv2.pyrDown(r1)
    cv2.imshow("Boyutlandırma", r1)
    cv2.waitKey(1000)

for a in range(5):
    r1 = cv2.pyrUp(r1)
    cv2.imshow("Boyutlandırma", r1)
    cv2.waitKey(1000)

cv2.waitKey(0)
cv2.destroyAllWindows()