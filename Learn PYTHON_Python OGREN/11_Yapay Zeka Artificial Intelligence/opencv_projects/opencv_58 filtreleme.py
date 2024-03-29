# filreleme
import cv2
import numpy as np

r1 = cv2.imread("images/top1.jpg")
r1 = cv2.pyrDown(r1)
cv2.imshow("Orjinal1", r1)

# np.array([hue, saturation, value])
alt = np.array([0,200,50]) # lower
ust = np.array([10,250,255]) # upper

hsv_sekli = cv2.cvtColor(r1, cv2.COLOR_BGR2HSV)
inrange_ile_maskeli_sekli = cv2.inRange(hsv_sekli, alt, ust)
inrange_ile_maskeli_sekli = cv2.medianBlur(inrange_ile_maskeli_sekli, 5)
filtreli_sekli = cv2.bitwise_and(r1, r1, mask = inrange_ile_maskeli_sekli)

# cv2.imshow("Cevrilmis1", c1)
# cv2.imshow("Cevrilmis2", c2)
cv2.imshow("Cevrilmis3(hsv_sekli)", hsv_sekli)
cv2.imshow("Cevrilmis4(filtreli_sekli)", filtreli_sekli)

cv2.imshow("inrange_ile_maskeli_sekli", inrange_ile_maskeli_sekli)
# cv2.imshow("bitwise_and ile", c5)

cv2.waitKey(0)
cv2.destroyAllWindows()


