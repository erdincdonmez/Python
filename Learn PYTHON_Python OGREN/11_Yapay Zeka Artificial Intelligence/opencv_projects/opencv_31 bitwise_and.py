# bitwise_and: Her ikisi de beyaz ise beyaz yap.
import cv2

r1 = cv2.imread("images/square1_600x400.png")
r2 = cv2.imread("images/ornekresim01_600x400.png")

bitwise_and_ile = cv2.bitwise_and(r1, r2)

cv2.imshow("Orjinal1 ", r1)
cv2.imshow("Orjinal2 ", r2)
cv2.imshow("bitwise_and_sekli ", bitwise_and_ile)

cv2.waitKey(0)
cv2.destroyAllWindows()
