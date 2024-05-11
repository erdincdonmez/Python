# pip install opencv-python
import cv2
import numpy as np

r1= np.full((50, 100, 3), [255, 0,255], dtype=np.uint8) # imshow ile BGR olarak görünür.
r2= np.full((50, 100, 3), [0, 250,0], dtype=np.uint8) # imshow ile BGR olarak görünür.
r4= np.full((50, 100, 3), [250, 250,0], dtype=np.uint8) # imshow ile BGR olarak görünür.
r3 = np.concatenate((r1, r2,r4))
# print(r3)
cv2.imshow("Olusan resim", r3)

cv2.waitKey(0)
 
# cv2.destroyAllWindows()