# boş resim oluşturma
import cv2
import numpy as np

# r1= np.full((yükseklik, genişlik, renk modu), [Mavi, Yeşil, Kırmızı], dtype=np.uint8)
r1= np.full((200, 300, 3), [255, 255, 255], dtype=np.uint8) # Beyaz
r2= np.full((200, 300, 3), [0, 0, 0], dtype=np.uint8) # Siyah
r3= np.full((200, 300, 3), [255, 0, 0], dtype=np.uint8) # Mavi
r4= np.full((200, 300, 3), [0, 255, 0], dtype=np.uint8) # Yeşil
r5= np.full((200, 300, 3), [0, 0, 255], dtype=np.uint8) # Kırmızı
r6= np.full((200, 300, 3), [0, 0, 50], dtype=np.uint8) # Kırmızı (açık)
r7= np.full((200, 300, 3), [0, 0, 255], dtype=np.uint8) # Kırmızı (yoğun)
r8= np.full((200, 300, 3), [50, 0, 50], dtype=np.uint8) # Mor (açık)
r9= np.full((200, 300, 3), [255, 0, 255], dtype=np.uint8) # Mor (yoğun)

cv2.imshow("Ak", r1)
cv2.imshow("Gara", r2)
cv2.imshow("Gok", r3)
cv2.imshow("Yasil", r4)
cv2.imshow("Kizil", r5)
cv2.imshow("Acik kirmizi", r6)
cv2.imshow("Tam kirmizi", r7)
cv2.imshow("Acik mor", r8)
cv2.imshow("Tam mor", r9)

cv2.waitKey(0)
 
cv2.destroyAllWindows() 