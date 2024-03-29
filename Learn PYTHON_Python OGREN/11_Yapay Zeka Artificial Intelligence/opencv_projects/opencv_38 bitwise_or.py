# bitwise_or: Birisi beyaz ise beyaz yap.
import cv2

r1 = cv2.imread("images/square1_600x400.png")
r2 = cv2.imread("images/ornekresim01_600x400.png")

bitwise_or_ile = cv2.bitwise_or(r1, r2)

cv2.imshow("Orjinal1 ", r1)
cv2.imshow("Orjinal2 ", r2)
cv2.imshow("bitwise_or_sekli ", bitwise_or_ile)

cv2.waitKey(0)
cv2.destroyAllWindows()
