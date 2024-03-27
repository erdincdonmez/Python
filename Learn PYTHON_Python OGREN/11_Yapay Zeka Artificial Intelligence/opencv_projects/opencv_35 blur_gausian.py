# GaussianBlur Görüntü parazitini ve ayrıntıları azaltır
import cv2

r1 = cv2.imread("images/square1_600x400.png")
# r1 = cv2.resize(r1,None, fx=0.5,fy=0.5)
blur_gaussian_ile = cv2.GaussianBlur(r1,(7,7),0)

cv2.imshow("Orjinal1", r1)
cv2.imshow("GaussianBlur ile", blur_gaussian_ile)

cv2.waitKey(0)
cv2.destroyAllWindows()