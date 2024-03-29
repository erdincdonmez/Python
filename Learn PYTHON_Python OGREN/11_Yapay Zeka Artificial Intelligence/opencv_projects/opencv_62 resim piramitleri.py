# pyrUp
import cv2
import numpy as np

r1 = cv2.imread("images/yesil_elma_1.jpg")
g, y, r = r1.shape
r1 = cv2.resize(r1, (g//10,y//10))
  
cv2.imshow("Orjinal1", r1)
r1 = cv2.pyrUp(r1)
cv2.imshow("Orjinal2", r1)
r1 = cv2.pyrUp(r1)
cv2.imshow("Orjinal3", r1)

cv2.waitKey(0)
cv2.destroyAllWindows()