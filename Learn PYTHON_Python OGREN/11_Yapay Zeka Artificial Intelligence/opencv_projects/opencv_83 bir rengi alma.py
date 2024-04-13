# BAKILACAK.
# cv2'de renk uzayları
import cv2, numpy as np

kaynak = cv2.VideoCapture(0)

while kaynak.isOpened():
    _, goruntu = kaynak.read()
    hsvSekli = cv2.cvtColor(goruntu, cv2.COLOR_BGR2HSV)
    cv2.imshow("Orjinal Goruntu", goruntu)

    cv2.namedWindow("Yesil renkler", cv2.WINDOW_NORMAL)
    yesil = np.uint8([[[0,255,0]]])
    hsv_yesil = cv2.cvtColor(yesil,cv2.COLOR_BGR2HSV)
    cv2.imshow("Yesil renkler", hsv_yesil)

    if cv2.waitKey(1) == ord("q"): break

cv2.destroyAllWindows()
