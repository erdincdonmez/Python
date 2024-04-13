# cv2'de renk uzayları
import cv2, numpy as np

kaynak = cv2.VideoCapture(0)

while kaynak.isOpened():
    _, goruntu = kaynak.read()
    hsvSekli = cv2.cvtColor(goruntu, cv2.COLOR_BGR2HSV)
    cv2.imshow("Orjinal Goruntu", goruntu)

    # HSV rekler opencv'de max 180dir.
    dusuk  = np.array([50,50,50]) # hsv min
    yuksek = np.array([70,255,255]) # hsv max
    maskeliSekli = cv2.inRange(hsvSekli, dusuk, yuksek)
    cv2.imshow("Meskeli Goruntu", maskeliSekli)

    araliktakiRenkler = cv2.bitwise_and(goruntu, goruntu, mask = maskeliSekli)
    cv2.imshow("Islenmis Goruntu", araliktakiRenkler)

    if cv2.waitKey(1) == ord("q"): break

cv2.destroyAllWindows()
