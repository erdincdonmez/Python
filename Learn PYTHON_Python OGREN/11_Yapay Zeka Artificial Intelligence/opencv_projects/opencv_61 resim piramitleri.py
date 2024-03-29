# pyrDown
import cv2
import numpy as np

r1 = cv2.imread("images/square1.jpg")
cv2.imshow("Orjinal1", r1)
r1 = cv2.pyrDown(r1)
cv2.imshow("Orjinal2", r1)
r1 = cv2.pyrDown(r1)
cv2.imshow("Orjinal3", r1)

cv2.waitKey(0)
cv2.destroyAllWindows()

