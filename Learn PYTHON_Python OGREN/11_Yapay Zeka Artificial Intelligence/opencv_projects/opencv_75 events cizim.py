# cv2'de eventlar
import cv2, numpy as np

mod = False
img = np.ones((400,600,3),np.uint8)

def ciz(event, x, y, flag, param):
    global mod
    if event == cv2.EVENT_LBUTTONDOWN: mod = True
    elif event == cv2.EVENT_LBUTTONUP: mod = False
    if event == cv2.EVENT_MOUSEMOVE: 
        if mod == True : cv2.circle(img,(x,y),5,(255,0,0),5)

    cv2.imshow("Fare olaylari",img)

while(1):
    cv2.namedWindow("Fare olaylari")
    cv2.setMouseCallback("Fare olaylari", ciz)
    if cv2.waitKey(1) & 0xFF == ord("q"): break

cv2.destroyAllWindows()
