# cv2'de trackbar
import cv2, numpy as np

def ciz(x): pass

img = np.ones((600,400,3),np.uint8)

cv2.namedWindow("Trackbar")

cv2.createTrackbar("Kirmizi","Trackbar",0,255,ciz)
cv2.createTrackbar("Yesil","Trackbar",0,255,ciz)
cv2.createTrackbar("Mavi","Trackbar",0,255,ciz)
cv2.createTrackbar("AC/KAPA","Trackbar",0,1,ciz)

while(1):
    cv2.imshow("Trackbar",img)
    cv2.setMouseCallback("Trackbar", ciz)

    a = cv2.getTrackbarPos("Kirmizi","Trackbar")
    b = cv2.getTrackbarPos("Yesil","Trackbar")
    c = cv2.getTrackbarPos("Mavi","Trackbar")
    d = cv2.getTrackbarPos("AC/KAPA","Trackbar")
    if d : img[:] = [c,b,a]
    else: img[0:0] = 0
    if cv2.waitKey(1) & 0xFF == ord("q"): break

cv2.destroyAllWindows()
