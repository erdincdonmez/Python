# Görüntü üzerinde çizim
import cv2, numpy as np, random

yukseklik, genislik = 400, 600
tus=""; sayac = 0

while tus!=ord("q"):
    resim = np.zeros((yukseklik,genislik,3),np.uint8)
    xx = cv2.FONT_HERSHEY_COMPLEX
    cv2.putText(resim,"OpenCV",(100,50),xx,2,(0,255,0),2)
    cv2.putText(resim,"erdincdonmez.com",(150,80),xx,.5,(0,0,255),1)    
    sayac += 1
    print (sayac)
    if sayac <2 or sayac%10 == 0 : 
        n1x = random.randint(0,genislik)
        n1y = random.randint(0,yukseklik)
        n2x = random.randint(0,genislik)
        n2y = random.randint(0,yukseklik)
        n3x = random.randint(0,genislik)
        n3y = random.randint(0,yukseklik)
        n4x = random.randint(0,genislik)
        n4y = random.randint(0,yukseklik)
        r,g,b = random.randint(0,255), random.randint(0,255), random.randint(0,255)
    noktalar = np.array([[n1x,n1y],[n2x,n2y],[n3x,n3y],[n4x,n4y]],np.int32)
    cv2.polylines(resim,[noktalar],True,(b,g,r),4)
    cv2.imshow("Resim olusturma",resim)
    tus = cv2.waitKey(100)

cv2.destroyAllWindows()