# trasformation/bükme
import cv2, numpy as np

goruntu = cv2.imread('images/square1_600x400.png')
cv2.imshow("Orjinal Goruntu", goruntu)

sutun, satir = goruntu.shape[:2]

# float32([[solüst x,y],[solalt x,y],[sağalt x,y]])
baslangic = np.float32([[50,50],[sutun,0],[0,satir]])
yeniyer   = np.float32([[90,90],[sutun//2,100],[200,satir//2]])

bukmeSekli = cv2.getAffineTransform(baslangic,yeniyer)
bukulmusSekli = cv2.warpAffine(goruntu, bukmeSekli, (satir,sutun))

cv2.imshow("Bukulmus sekli", bukulmusSekli)

cv2.waitKey(0)
cv2.destroyAllWindows()
