# Video açma
import cv2

# cap = cv2.VideoCapture('videolar/ornek1_dunya.mp4')
cap = cv2.VideoCapture(0)
# tekGoruntu = cv2.imread('resimler/bayrak2.jpg')
# ret = True
while cap.isOpened():
    ret, tekGoruntu = cap.read()
    if ret == True:
        # tekGoruntu = cv2.transpose(tekGoruntu)
        m, y, k = cv2.split(tekGoruntu)

        cv2.imshow("Orjinal     ", tekGoruntu)
        cv2.imshow("Maviler     ", m)
        # cv2.imshow("Yeşiller    ", y)
        cv2.imshow("Kirmizilar  ", k)
        # cv2.imshow('tekGoruntu',tekGoruntu)
        tus = cv2.waitKey(1)
        if tus == ord('q'): break
    else: break

cap.release()
cv2.destroyAllWindows()

