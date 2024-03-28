# threshold - THRESH_BINARY
import cv2

r1 = cv2.imread("images/yesil_elma_1.jpg", 0)

a, c1 = cv2.threshold(r1, 190, 255, cv2.THRESH_BINARY)
a, c2 = cv2.threshold(r1, 190, 255, cv2.THRESH_BINARY_INV)
a, c3 = cv2.threshold(r1, 190, 255, cv2.THRESH_TOZERO)
a, c4 = cv2.threshold(r1, 190, 255, cv2.THRESH_TOZERO_INV)
r1 = cv2.resize(r1, (300, 300))

cv2.imshow("Orjinal1", r1)
cv2.imshow("THRESH_BINARY sekli", cv2.resize(c1, (300, 300)))
cv2.imshow("THRESH_BINARY_INV sekli", cv2.resize(c2, (300, 300)))
cv2.imshow("THRESH_TOZERO sekli", cv2.resize(c3, (300, 300)))
cv2.imshow("THRESH_TOZERO_INV sekli", cv2.resize(c4, (300, 300)))

cv2.waitKey(0)
cv2.destroyAllWindows()


