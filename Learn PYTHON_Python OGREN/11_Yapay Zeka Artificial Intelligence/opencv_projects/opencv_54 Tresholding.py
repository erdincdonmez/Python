# threshold - THRESH_BINARY
import cv2

r1 = cv2.imread("images/yesil_elma_1.jpg", 0)
cv2.imshow("Orjinal1", r1)

for a in range(255):
    _, Cevrilmis = cv2.threshold(r1, a, 255, cv2.THRESH_BINARY)
    cv2.imshow("Cevrilmis şekli", Cevrilmis)
    cv2.waitKey(30)
     
cv2.destroyAllWindows()

import matplotlib.pyplot as plt


