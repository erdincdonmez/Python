# inpaint mask
import cv2

r1 = cv2.imread("images/square1_600x400.png")
r2 = cv2.imread("images/ornekresim01_600x400.png",0)
cv2.imshow("Orjinal1", r1)
cv2.imshow("Orjinal2", r2)

_, c1 = cv2.threshold(r2, 200, 255, cv2.THRESH_BINARY)
_, c2 = cv2.threshold(r2, 200, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Cevrilmis1", c1)
cv2.imshow("Cevrilmis2", c2)

f1 = cv2.inpaint(r1, c1, 2, cv2.INPAINT_NS)
cv2.imshow("inpaint ile1", f1)
f2 = cv2.inpaint(r1, c2, 2, cv2.INPAINT_NS)
cv2.imshow("inpaint ile2", f2)


cv2.waitKey(0)
cv2.destroyAllWindows()


