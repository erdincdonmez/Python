# boş resim oluşturma
import cv2, random
import numpy as np
# max = 300
m = random.randint(0,255);
y = random.randint(0,255); k = random.randint(0,255);
# r1= np.full((max, max, 3), [m, y, k], dtype=np.uint8)
r1 = cv2.imread('resimler/bayrak2.jpg')
h, w, c = r1.shape
max = h
print(h,w,c)

for a in range (max):
    for b in range(a, max):
      xyr = r1[a,b]
      # print(xyr)
      r1[a,b] = [xyr[0],xyr[1],xyr[2]+20]
      if a == b : r1[a,b] = [0, 0, 0]
      if a == b//2 : r1[a,b] = [255, 255, 255]
      # if b == max-20 : r1[a,b] = [0, 0, 255]

for c in range(100):
   m1=random.randint(0,255); y1=random.randint(0,255); k1=random.randint(0,255);
   x = random.randint(3,max-3); y = random.randint(3,max-3)
   r1[x-1, y-1] = [m1, y1, k1]
   r1[x-1, y] = [m1, y1, k1]
   r1[x-1, y+1] = [m1, y1, k1]
   r1[x, y-1] = [m1, y1, k1]
   r1[x, y] = [m1, y1, k1]
   r1[x, y+1] = [m1, y1, k1]
   r1[x+1, y-1] = [m1, y1, k1]
   r1[x+1, y] = [m1, y1, k1]
   r1[x+1, y+1] = [m1, y1, k1]

cv2.imshow("Resim", r1)
r2 = cv2.transpose(r1)
cv2.imshow("Resim1", r2)
cv2.waitKey(0)
cv2.destroyAllWindows()

