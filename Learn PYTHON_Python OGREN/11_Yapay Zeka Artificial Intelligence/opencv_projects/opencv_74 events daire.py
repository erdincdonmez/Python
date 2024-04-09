# cv2'de eventlar
import cv2, numpy as np

xx=yy=0
img = np.ones((400,600,3),np.uint8)
parca = np.ones((30,120,3),np.uint8)
def draw(event, x, y, flag, param):
    global xx, yy
    xx,yy = x,y
    # print("x:",x," y:",y)
    img[0:30, 0:120] = parca
    cv2.putText(img,f"x:{x} y:{y}",(10,20),cv2.FONT_HERSHEY_COMPLEX,.5,(0,0,255),1) 
    if event == cv2.EVENT_FLAG_LBUTTON: cv2.circle(img,(x,y),30,(255,150,50),2)
    cv2.imshow("Fare olaylari",img)

while(1):
    cv2.namedWindow("Fare olaylari")
    cv2.setMouseCallback("Fare olaylari", draw)
    if cv2.waitKey(1) & 0xFF == ord("q"): break

cv2.destroyAllWindows()
