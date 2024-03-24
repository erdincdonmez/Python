# Kameraya erişme (saniyede bir)
import cv2

cap = cv2.VideoCapture('videos/wildlife.mp4')

if cap.isOpened() == False: print("video açılamadı")

while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow('frame',frame)
        tus = cv2.waitKey(20) # 1000/30 = 33
        if tus == ord('q'): break
    else: break
cap.release()
cv2.destroyAllWindows()



