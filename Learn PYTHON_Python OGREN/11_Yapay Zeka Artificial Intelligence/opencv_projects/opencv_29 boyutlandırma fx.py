# Yeniden boyutlandırma fx ile
import cv2
r1 = cv2.imread('images/ornekresim01_600x400.png')
cv2.imshow('Orjinal resim:', r1)
print("Resim boyutu:", r1.shape)

r1Boyutlandirilmis = cv2.resize(r1, (300,200))
cv2.imshow('Boyulandirilmis', r1Boyutlandirilmis)
print("Resim boyutu", r1Boyutlandirilmis.shape)

# Boyutlandirilmisfxile = cv2.resize(r1, (g*2,y*2))
Boyutlandirilmisfxile = cv2.resize(r1, None, fx=.5, fy=1)
cv2.imshow('fx ile boyutlandirilmis', Boyutlandirilmisfxile)

cv2.waitKey(0)
cv2.destroyAllWindows()