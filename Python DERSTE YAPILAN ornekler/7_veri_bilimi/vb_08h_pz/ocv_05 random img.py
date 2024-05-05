# rastgele iki renkli resim oluşturma
import cv2, random
import numpy as np

tus = 65
while tus != ord('q'): # ord('q') q ya basılana kadar
  print("\nKapatmak için q tuşuna basın..")
  m1 = random.randint(0,255);
  y1 = random.randint(0,255); k1 = random.randint(0,255);
  m2 = random.randint(0,255);
  y2 = random.randint(0,255); k2 = random.randint(0,255);
 
  r1= np.full((200, 300, 3), [m1, y1, k1], dtype=np.uint8)
  r2= np.full((200, 300, 3), [m2, y2, k2], dtype=np.uint8)
  r3 = np.concatenate((r1, r2,r1))
  cv2.imshow("Resim", r3)
  print(f"Mavi:{m1}, Yeşil:{y1}, Kırmızı:{k1}")
  print(f"Mavi:{m2}, Yeşil:{y2}, Kırmızı:{k2}")
  tus = cv2.waitKey(0)

cv2.destroyAllWindows()