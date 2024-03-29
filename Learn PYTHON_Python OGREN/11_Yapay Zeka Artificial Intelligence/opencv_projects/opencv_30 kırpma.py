# Yeniden boyutlandırma
import cv2
import matplotlib.pyplot as plt
r1 = cv2.imread('images/ornekresim01_150x100.png')

r1Kesilmis = r1[0:50,0:50]
cv2.imshow('Resim boyutlandırma:', r1Kesilmis)
r1Kesilmis2 = r1[:70,:90]
cv2.imshow('Resim boyutlandırma:', r1Kesilmis2)

cv2.waitKey(0)
cv2.destroyAllWindows()