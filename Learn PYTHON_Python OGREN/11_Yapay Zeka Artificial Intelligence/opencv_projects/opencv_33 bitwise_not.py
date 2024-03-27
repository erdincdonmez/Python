# bitwise_not
import cv2

r1 = cv2.imread("images/square1_600x400.png")
r2 = cv2.imread("images/ornekresim01_600x400.png")

bitwise_not_ile1 = cv2.bitwise_not(r1)
bitwise_not_ile2 = cv2.bitwise_not(r2)

cv2.imshow("Orjinal1 ", r1)
cv2.imshow("Orjinal2 ", r2)
cv2.imshow("bitwise_not_sekli1 ", bitwise_not_ile1)
cv2.imshow("bitwise_not_sekli2 ", bitwise_not_ile2)

cv2.waitKey(0)
cv2.destroyAllWindows()
