# Video açma
import cv2

cap = cv2.VideoCapture('videolar/ornek1_dunya.mp4')

while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:
        # frame = cv2.transpose(frame)
        cv2.imshow('frame',frame)
        tus = cv2.waitKey(1)
        if tus == ord('q'): break
    else: break

cap.release()
cv2.destroyAllWindows()

