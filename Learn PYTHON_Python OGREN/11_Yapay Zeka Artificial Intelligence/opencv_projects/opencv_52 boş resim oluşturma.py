# boş resim oluşturma
import cv2
import numpy as np

for a in range(0,255,10):
  for b in range(0,255,10):
    for c in range(0,255,10):
      r1= np.full((200, 300, 3), [a, b, c], dtype=np.uint8) 
      cv2.imshow("Resim", r1)
      print(f"Mavi:{a}, Yeşil:{b}, Kırmızı:{c}")
      cv2.waitKey(1)
 
cv2.destroyAllWindows() 