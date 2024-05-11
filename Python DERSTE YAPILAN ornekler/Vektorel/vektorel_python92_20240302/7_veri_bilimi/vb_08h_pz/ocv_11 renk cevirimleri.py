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
        cevrilmis = cv2.cvtColor(tekGoruntu, cv2.COLOR_BGR2HSV)
        cevrilmis2 = cv2.cvtColor(tekGoruntu, cv2.COLOR_BGRA2GRAY)
        cv2.imshow("Orjinal     ", tekGoruntu)
        cv2.imshow("Cevrilmis   ", cevrilmis)
        cv2.imshow("Cevrilmis2   ", cevrilmis2)

        tus = cv2.waitKey(1)
        if tus == ord('q'): break
    else: break

cap.release()
cv2.destroyAllWindows()

