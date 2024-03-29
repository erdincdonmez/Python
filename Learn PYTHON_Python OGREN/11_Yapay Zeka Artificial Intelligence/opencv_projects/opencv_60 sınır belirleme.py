import cv2
import numpy as np

r1 = cv2.imread("images/top1.jpg")
r1 = cv2.pyrDown(r1)
cv2.imshow("Orjinal1", r1)

# np.array([hue, saturation, value])
alt = np.array([0,100,10]) # lower
ust = np.array([10,250,255]) # upper

hsv_sekli = cv2.cvtColor(r1, cv2.COLOR_BGR2HSV)
maskeli_sekli = cv2.inRange(hsv_sekli, alt, ust)
maskeli_sekli = cv2.medianBlur(maskeli_sekli, 5)

kenarlari, _ = cv2.findContours(maskeli_sekli, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
# kenarlari, _ = cv2.findContours(maskeli_sekli, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for cnt in kenarlari:
    x,y,w,h = cv2.boundingRect(cnt)
    cv2.rectangle(r1,(x,y),(x+w,y+h),[0,0,255],4)

    for i in cnt:
        x,y = i[0]
        r1[y,x] = [0,0,255]

cv2.imshow("HSV goruntusu", hsv_sekli)
cv2.imshow("Maskelenmis goruntu", maskeli_sekli)
cv2.imshow("Kenarlar", r1)

filtreli_sekli = cv2.bitwise_and(r1, r1, mask = maskeli_sekli)
cv2.imshow("Kenarlar", filtreli_sekli)


cv2.waitKey(0)
cv2.destroyAllWindows()
