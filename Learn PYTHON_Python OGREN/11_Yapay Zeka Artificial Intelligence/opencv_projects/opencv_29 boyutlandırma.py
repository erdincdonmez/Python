# Yeniden boyutlandırma
import cv2
import matplotlib.pyplot as plt
r1 = cv2.imread('images/ornekresim01_150x100.png')

print("Resim boyutu:", r1.shape)
r1Boyutlandirilmis = cv2.resize(r1, (200,300))
print("Resim boyutu:", r1Boyutlandirilmis.shape)
g, y, r = r1.shape
r1Boyutlandirilmis2 = cv2.resize(r1, (g*2,y*2))

cv2.imshow('Resim boyutlandırma:', r1)
cv2.imshow('Resim boyutlandırma:', r1Boyutlandirilmis)
cv2.imshow('Resim boyutlandırma:', r1Boyutlandirilmis2)

cv2.waitKey(0)
cv2.destroyAllWindows()