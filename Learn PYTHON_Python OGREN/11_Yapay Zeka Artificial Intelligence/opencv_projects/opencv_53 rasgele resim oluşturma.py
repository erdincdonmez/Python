# boş resim oluşturma
import cv2, random
import numpy as np

tus = 65
while tus != ord('q'): # ord('q') q ya basılana kadar
  print("\nKapatmak için q tuşuna basın..")
  # ; ile birden çok komut tek satıra yazılabilir.
  m = random.randint(0,255); 
  y = random.randint(0,255); k = random.randint(0,255); 
  r1= np.full((200, 300, 3), [m, y, k], dtype=np.uint8) 
  cv2.imshow("Resim", r1)
  print(f"Mavi:{m}, Yeşil:{y}, Kırmızı:{k}")
  tus = cv2.waitKey(0)

# cv2.waitKey(0) # bir tuşa basılana kadar bekle
cv2.destroyAllWindows() 