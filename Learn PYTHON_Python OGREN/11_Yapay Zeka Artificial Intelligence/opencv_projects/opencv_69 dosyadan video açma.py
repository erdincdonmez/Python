# Dosyadan okuma ve renksizleştirme
import cv2

videoDosyasi = cv2.VideoCapture('videos/wildlife.mp4')

if videoDosyasi.isOpened() == False: print("video açılamadı")

while videoDosyasi.isOpened():
    durum, okunan = videoDosyasi.read()
    okunanSB = cv2.cvtColor(okunan, cv2.COLOR_BGR2GRAY)
    if durum == True:
        cv2.imshow('okunan goruntu',okunan)
        cv2.imshow('okunan renksiz',okunanSB)
        tus = cv2.waitKey(20) # 1000/30 = 33
        if tus == ord('q'): exit()
    else: break
videoDosyasi.release()
cv2.destroyAllWindows()



