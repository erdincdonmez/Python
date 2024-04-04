# Video recording
import cv2

kamera = cv2.VideoCapture(0)
kodekli = cv2.VideoWriter_fourcc(*'XVID') # fourcc.org/
# genislik  = int(vid.get(3))
# yukseklik = int(vid.get(4))
# boyut = (genislik, yukseklik)

sonuc = cv2.VideoWriter('videos/kayit2.avi',kodekli,30.0,(640,480))
print("Kayıt tamamlandı.")

while kamera.isOpened():
    ret, okunan = kamera.read()
    if ret == True:
        sonuc.write(okunan)
        cv2.imshow('okunan goruntu',okunan)

        tus = cv2.waitKey(1)
        if tus == ord('s'): exit()
    else: break

kamera.release()
sonuc.release()
cv2.destroyAllWindows()