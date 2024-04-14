# traspose işlemi
import cv2, numpy as np

goruntu = cv2.imread('images/square1_600x400.png')
cv2.imshow("Orjinal Goruntu", goruntu)

trasposeSekli = cv2.transpose(goruntu)
cv2.imshow("Traspose sekli", trasposeSekli)

cv2.waitKey(0)
cv2.destroyAllWindows()
