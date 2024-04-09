# Görüntü üzerinde çizim
import cv2, numpy as np

# resim = np.zeros((1000,600,3),dtype=np.uint8)
resim = np.zeros((400,600,3),np.uint8)
cv2.line(resim,(0,0),(600,400),(0,0,255),2)
cv2.line(resim,(600,0),(0,400),(0,0,255),2)

cv2.circle(resim,(300,200),100,(255,255,255),2)

cv2.rectangle(resim,(100,100),(150,150),(255,0,0),-1)
cv2.rectangle(resim,(200,100),(400,300),(255,0,0),3)

cv2.ellipse(resim,(500,50),(50,25),0,0,180,(255,0,0),2)
cv2.ellipse(resim,(500,150),(50,25),0,0,180,(255,0,0),-1)
cv2.ellipse(resim,(500,250),(50,25),0,0,360,(0,255,0),2)
cv2.ellipse(resim,(500,350),(50,25),0,0,360,(0,255,255),-1)

noktalar = np.array([[20,30],[70,150],[200,250],[50,300]],np.int32)
# noktalar2 = noktalar.reshape(-1,1,2)
# cv2.polylines(resim,[noktalar],False,(0,200,200),4)
cv2.polylines(resim,[noktalar],True,(0,200,200),4)

xx = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(resim,"OpenCV",(100,50),xx,2,(0,255,0),2)
cv2.putText(resim,"erdincdonmez.com",(150,80),xx,.5,(0,0,255),1)
# cv2.putText(resim,"FPS:60",(100,200),xx,.5,(0,255,0),2,cv2.LINE_AA)

cv2.imshow("Resim olusturma",resim)
cv2.waitKey(0)
cv2.destroyAllWindows()