import cv2

cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()

    if not ret:
        print("Kameradan görüntü okunamıyor.")
        break
    cv2.imshow("Goruntu",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Görüntü kapatıldı")
        break
cam.release()
cv2.destroyAllWindows()
