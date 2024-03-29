
# ctvColor
import cv2

r1 = cv2.imread("images/square1_600x400.png")
# cv2.cvtColor(r1, cv2.COLOR_ ... alternatiflerini deneyin
Cevrilmis = cv2.cvtColor(r1, cv2.COLOR_BGR2HSV)

cv2.imshow("Orjinal1", r1)
cv2.imshow("Cevrilmis şekli", Cevrilmis)

cv2.waitKey(0)
cv2.destroyAllWindows()
