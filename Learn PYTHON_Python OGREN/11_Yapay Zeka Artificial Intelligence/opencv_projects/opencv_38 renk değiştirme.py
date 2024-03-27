
# ctvColor
import cv2

r1 = cv2.imread("images/square1_600x400.png")
graysclale1 = cv2.cvtColor(r1, cv2.COLOR_BGR2GRAY)

cv2.imshow("Orjinal1", r1)
cv2.imshow("graysclale1 ile", graysclale1)

cv2.waitKey(0)
cv2.destroyAllWindows()
