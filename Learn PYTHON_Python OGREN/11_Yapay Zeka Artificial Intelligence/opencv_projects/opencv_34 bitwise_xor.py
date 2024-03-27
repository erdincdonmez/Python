# bitwise_xor
import cv2

r1 = cv2.imread("images/square1_600x400.png")
r2 = cv2.imread("images/ornekresim01_600x400.png")

bitwise_xor_ile1 = cv2.bitwise_xor(r1,r2)

cv2.imshow("Orjinal1 ", r1)
cv2.imshow("Orjinal2 ", r2)
cv2.imshow("bitwise_xor_sekli1 ", bitwise_xor_ile1)

cv2.waitKey(0)
cv2.destroyAllWindows()
