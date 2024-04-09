# cv2'de eventlar
import cv2, numpy as np

xx=yy=0
mod = ""
img = np.ones((400,600,3),np.uint8)
parca = np.ones((30,120,3),np.uint8)
basx=basy=sonx=sony = -1
def ciz(event, x, y, flag, param):
    global xx,yy,mod,basx,basy,sonx,sony
    xx,yy = x,y
    
    # print("x:",x," y:",y)
    img[0:30, 0:120] = parca
    fontu = cv2.FONT_HERSHEY_COMPLEX
    cv2.putText(img,f"x:{x} y:{y}",(10,20),fontu,.5,(0,0,255),1) 
    cv2.putText(img,"daire",(200,20),fontu,.5,(255,0,0),1) 
    cv2.putText(img,"dikdortgen",(300,20),fontu,.5,(0,255,0),1) 
    cv2.putText(img,"cikis",(550,20),fontu,.5,(0,0,255),1) 
    if event == cv2.EVENT_FLAG_LBUTTON and (x > 200 and x<300) and (y>0 and y<30): 
        mod = "daire"; print(mod)
    elif event == cv2.EVENT_FLAG_LBUTTON and (x > 300 and x<400) and (y>0 and y<30): 
        mod = "dortgen"; print(mod) 
    else:
        # if event == cv2.EVENT_FLAG_LBUTTON: cv2.circle(img,(x,y),30,(255,150,50),2)
        img[0:30, 400:540] = np.ones((30,140,3),np.uint8)
        cv2.putText(img,f"Mod:{mod}",(400,20),fontu,.5,(0,255,255),1) 
        if event == cv2.EVENT_LBUTTONDOWN: 
            ciz == True  
            if basx < 0 : basx = x; basy = y
            print(f"basx:{basx} basy:{basy}")

        if event == cv2.EVENT_MOUSEMOVE:
            if basx > 0 and mod == "daire": 
                cv2.circle(img,(basx,basy),x-basx-1,(0,0,00),5)
                cv2.circle(img,(basx,basy),x-basx,(255,150,50),2)

            if basx > 0 and mod == "dortgen": 
                cv2.rectangle(img,(basx,basy),(x-2,y-1),(0,0,0),5)
                cv2.rectangle(img,(basx,basy),(x,y),(255,0,0),2)

        if event == cv2.EVENT_LBUTTONUP: 
            ciz == False
            if sonx < 0 : 
                sonx = x; sony = y
                print(f"sonx:{sonx} sony:{sony}")
                if mod == "daire": cv2.circle(img,(basx,basy),sonx-basx,(255,150,50),2)        
                if mod == "dortgen": cv2.rectangle(img,(basx,basy),(sonx,sony),(255,0,0),2)     
                basx=basy=sonx=sony = -1
    
    cv2.imshow("Fare olaylari",img)

while(1):
    cv2.namedWindow("Fare olaylari")
    cv2.setMouseCallback("Fare olaylari", ciz)
    if cv2.waitKey(1) & 0xFF == ord("q"): break

cv2.destroyAllWindows()
