# threshold - THRESH_BINARY
import cv2

r1 = cv2.imread("images/yesil_elma_1.jpg", 0)

a, Cevrilmis = cv2.threshold(r1, 190, 255, cv2.THRESH_BINARY)

cv2.imshow("Orjinal1", r1)
cv2.imshow("Cevrilmis şekli", Cevrilmis)

cv2.waitKey(0)
cv2.destroyAllWindows()


