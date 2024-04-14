# perspective trasformation/bükme
import cv2, numpy as np

goruntu = cv2.imread('images/sudoku368x340.JPG')
cv2.imshow("Orjinal Goruntu", goruntu)

sutun, satir = goruntu.shape[:2]
print(satir,sutun)

# float32([[üstsol x,y],[üstsağ x,y],[altsol x,y],[altsağ x,y]])
baslangic = np.float32([[50,60],[300,50],[30,310],[325,300]])
yeniyer = np.float32([[0,0],[sutun,0],[0,satir],[sutun,satir]])

bukmeSekli = cv2.getPerspectiveTransform(baslangic,yeniyer)
bukulmusSekli = cv2.warpPerspective(goruntu, bukmeSekli, (satir,sutun))

cv2.imshow("Bukulmus sekli", bukulmusSekli)

cv2.waitKey(0)
cv2.destroyAllWindows()
