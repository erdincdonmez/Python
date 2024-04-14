# görüntüyü kaydırma
import cv2, numpy as np

kaynak = cv2.VideoCapture(0)

while kaynak.isOpened():
    _, goruntu = kaynak.read()

    satir, sutun = goruntu.shape[:2]

    kaymaSekli = np.float32([[1,0,30],[0,1,30]])

    kaymisSekli = cv2.warpAffine(goruntu,kaymaSekli,(sutun+40, satir+40))

    cv2.imshow("Orjinal Goruntu", goruntu)
    cv2.imshow("Kaymis sekli", kaymisSekli)

    if cv2.waitKey(1) == ord("q"): break

cv2.destroyAllWindows()
