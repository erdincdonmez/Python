# rotation/döndürme işlemi
import cv2, numpy as np

goruntu = cv2.imread('images/square1_600x400.png')
cv2.imshow("Orjinal Goruntu", goruntu)

sutun, satir = goruntu.shape[:2]

# cv2.getRotationMatrix2D((dönme merkezi x,y),açı,yaklaştırma)
donmeSekli = cv2.getRotationMatrix2D((satir//2,sutun//2),30,.5)
donmusSekli = cv2.warpAffine(goruntu, donmeSekli, (satir,sutun))

cv2.imshow("Cevirilmis sekli", donmusSekli)

cv2.waitKey(0)
cv2.destroyAllWindows()
