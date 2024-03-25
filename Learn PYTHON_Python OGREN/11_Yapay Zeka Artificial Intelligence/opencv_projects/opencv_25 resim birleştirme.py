# Resim birleştirme
import cv2
import matplotlib.pyplot as plt
r1 = cv2.imread('images/ornekresim01_600x400.png')
r2 = cv2.imread('images/square1_600x400.png')

birlesik = cv2.add(r1, r2)

cv2.imshow('Resim birleştirme:', birlesik)

print("Resim1[10,20] renkleri:",r1[10,20])
print("Resim2[10,20] renkleri:",r2[10,20])
print("birlesik[10,20] renkleri:",birlesik[10,20])

cv2.waitKey(0)
cv2.destroyAllWindows()