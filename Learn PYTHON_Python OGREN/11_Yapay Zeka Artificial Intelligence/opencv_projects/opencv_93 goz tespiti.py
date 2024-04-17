# göz tespiti
import cv2

goz_bulma = cv2.CascadeClassifier("data/haarcascades/haarcascade_eye.xml")
# kaynak = cv2.VideoCapture('http://192.168.1.7:8080/video')
kaynak = cv2.VideoCapture(0)

while kaynak.isOpened():

    durum, goruntu = kaynak.read()
    if durum:
        goruntu = cv2.resize(goruntu,None,fx=1/2,fy=1/2,interpolation=cv2.INTER_AREA)
    
    goruntu_griton = cv2.cvtColor(goruntu, cv2.COLOR_BGR2GRAY)
    goruntu_griton = cv2.equalizeHist(goruntu_griton)
    yuzler = goz_bulma.detectMultiScale(goruntu_griton)

    for (x,y,w,h) in yuzler:
        merkez = (x+w//2,y+h//2)
        goruntu = cv2.ellipse(goruntu, merkez, (w//2,h//2),0,0,360,(0,255,0),4)

    cv2.imshow("Yuz tespiti", goruntu)

    if cv2.waitKey(1) == ord("q") : break

cv2.destroyAllWindows()
