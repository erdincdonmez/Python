# denoising (gürültü giderme)
import cv2

r1 = cv2.imread("images/tacmahal_noised.jpg", 0)
cv2.imshow("Orjinal1", r1)

g1 = cv2.fastNlMeansDenoising(r1, None, 15, 10, 10)
cv2.imshow("denoised", g1)

cv2.waitKey(0)
cv2.destroyAllWindows()


