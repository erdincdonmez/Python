# cv2'de renk uzayları
import cv2, numpy as np

kaynak = cv2.VideoCapture(0)

def fonksiyon(): pass

cv2.namedWindow("Orjinal Goruntu")
cv2.createTrackbar("Hue min", "Orjinal Goruntu", 0, 359, fonksiyon)
cv2.createTrackbar("Hue max", "Orjinal Goruntu", 0, 359, fonksiyon)
cv2.createTrackbar("Saturation min", "Orjinal Goruntu", 0, 255, fonksiyon)
cv2.createTrackbar("Saturation max", "Orjinal Goruntu", 0, 255, fonksiyon)
cv2.createTrackbar("Value min", "Orjinal Goruntu", 0, 255, fonksiyon)
cv2.createTrackbar("Value max", "Orjinal Goruntu", 0, 255, fonksiyon)

while kaynak.isOpened():
    _, goruntu = kaynak.read()
    hsvSekli = cv2.cvtColor(goruntu, cv2.COLOR_BGR2HSV)
    cv2.imshow("Orjinal Goruntu", goruntu)

    h1 = cv2.getTrackbarPos("Hue min","Orjinal Goruntu") // 2
    h2 = cv2.getTrackbarPos("Hue max","Orjinal Goruntu") // 2
    s1 = cv2.getTrackbarPos("Saturation min","Orjinal Goruntu")
    s2 = cv2.getTrackbarPos("Saturation max","Orjinal Goruntu")
    v1 = cv2.getTrackbarPos("Value min","Orjinal Goruntu")
    v2 = cv2.getTrackbarPos("Value max","Orjinal Goruntu")

    # HSV rekler opencv'de max 180dir.
    dusuk  = np.array([h1,s1,v1]) # hsv min
    yuksek = np.array([h1,s1,v2]) # hsv max
    maskeliSekli = cv2.inRange(hsvSekli, dusuk, yuksek)
    cv2.imshow("Meskeli Goruntu", maskeliSekli)

    islenmisSekli = cv2.bitwise_and(goruntu, goruntu, mask = maskeliSekli)
    cv2.imshow("Islenmis Goruntu", islenmisSekli)

    if cv2.waitKey(1) == ord("q"): break

cv2.destroyAllWindows()
