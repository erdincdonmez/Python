# Video recording
import cv2

vid = cv2.VideoCapture(0)

genislik  = int(vid.get(3))
yukseklik = int(vid.get(4))
boyut = (genislik, yukseklik)

# fourcc.org/
sonuc = cv2.VideoWriter('videos/kayit1.avi',cv2.VideoWriter_fourcc(*'XVID'),20, boyut)
print("Kayıt tamamlandı.")

while True:
    ret, frame = vid.read()
    if ret == True:
        sonuc.write(frame)
        cv2.imshow('frame',frame)

        tus = cv2.waitKey(1)
        if tus == ord('s'): break
    else: break

vid.release()
sonuc.release()
cv2.destroyAllWindows()