# pip install opencv-python
# boş resim oluşturma
import cv2
import numpy as np

# aşağıdaki [255, 255, 255] rakamlarını oynayarak ne olduğuna bakın
# r1= np.full((10, 10), [200], dtype=np.uint8)
r1= np.full((100, 100, 3), [255, 0,255], dtype=np.uint8) # imshow ile BGR olarak görünür.
print(r1)
cv2.imshow("Olusan resim", r1)

# for a in range(250):
#     r1= np.full((300, 300, 3), [0, a, 0], dtype=np.uint8)
#     print(r1)
#     cv2.waitKey(100)
#     cv2.imshow("Olusan resim", r1)

cv2.waitKey(0)
 
# cv2.destroyAllWindows()