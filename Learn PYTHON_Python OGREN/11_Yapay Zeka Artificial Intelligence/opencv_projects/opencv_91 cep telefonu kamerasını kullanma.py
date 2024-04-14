# cep telefonu kamerasından görüntü alma
import cv2

# kaynak = cv2.VideoCapture('http://192.168.1.7:8080/video')
kaynak = cv2.VideoCapture('http://192.168.1.4:8888/video')

while kaynak.isOpened():

    durum, goruntu = kaynak.read()
    cv2.imshow("Orjinal Goruntu", goruntu)

    if cv2.waitKey(1) == ord("q") : break

cv2.destroyAllWindows()
