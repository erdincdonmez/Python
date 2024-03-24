# Kameraya erişme (saniyede bir)
import cv2

vid = cv2.VideoCapture(0) # 1, 2 diğer kamerlalar

while True:
    ret, frame = vid.read()
    cv2.imshow('frame',frame)
    # tus = cv2.waitKey(0) # bekleme süresi
    tus = cv2.waitKey(1000) # bir saniye bekle
    if tus == ord('q'): break

vid.release()
cv2.destroyAllWindows()

