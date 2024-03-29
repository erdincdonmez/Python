# erode
import cv2
import numpy as np

r1 = cv2.imread("images/square1_600x400.png")
cekirdek = np.ones((5,5),np.uint8)

Cevrilmis = cv2.erode(r1, cekirdek)

cv2.imshow("Orjinal1", r1)
cv2.imshow("Cevrilmis şekli", Cevrilmis)

cv2.waitKey(0)
cv2.destroyAllWindows()
