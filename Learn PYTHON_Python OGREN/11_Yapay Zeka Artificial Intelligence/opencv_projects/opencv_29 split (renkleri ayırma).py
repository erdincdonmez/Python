import cv2

r = cv2.imread("images/ornekresim01_600x400.png")

m, y, k = cv2.split(r)

cv2.imshow("Orjinal     ", r)
cv2.imshow("Maviler     ", m)
cv2.imshow("Yeşiller    ", y)
cv2.imshow("Kırmızılar  ", k)

cv2.waitKey(0)
cv2.destroyAllWindows()