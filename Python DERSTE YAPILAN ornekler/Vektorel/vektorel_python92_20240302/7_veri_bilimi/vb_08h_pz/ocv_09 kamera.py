# Video açma
import cv2

# cap = cv2.VideoCapture('videolar/ornek1_dunya.mp4')
kaynak = cv2.VideoCapture(0)

while kaynak.isOpened():
    ret, tekGoruntu = kaynak.read()
    if ret == True:
        sonuc = cv2.transpose(tekGoruntu)
        cv2.imshow('Pencere1',tekGoruntu)
        cv2.imshow('Pencere2',sonuc)
        tus = cv2.waitKey(1)
        if tus == ord('q'): break
    else: break

kaynak.release()
cv2.destroyAllWindows()

