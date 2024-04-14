# resmi kaydırma
import cv2, numpy as np

goruntu = cv2.imread('images/square1_600x400.png')

satir, sutun = goruntu.shape[:2]

kaymaSekli = np.float32([[1,0,30],[0,1,30]])

kaymisSekli = cv2.warpAffine(goruntu,kaymaSekli,(sutun+40, satir+40))

cv2.imshow("Orjinal Goruntu", goruntu)
cv2.imshow("Kaymis sekli", kaymisSekli)

cv2.waitKey(0)

cv2.destroyAllWindows()
