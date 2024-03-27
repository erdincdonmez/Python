# bilateralFilter
import cv2

r1 = cv2.imread("images/square1_600x400.png")
bilateralFilter_ile = cv2.bilateralFilter(r1,9,75,75)

cv2.imshow("Orjinal1", r1)
cv2.imshow("bilateralFilter ile", bilateralFilter_ile)

cv2.waitKey(0)
cv2.destroyAllWindows()

