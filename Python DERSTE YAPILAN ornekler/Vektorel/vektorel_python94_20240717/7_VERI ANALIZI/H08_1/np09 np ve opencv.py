import cv2
import numpy as np

# aşağıdaki [255, 255, 255] rakamlarını oynayarak ne olduğuna bakın
r1= np.full((500, 500, 3), [255, 0, 255], dtype=np.uint8)
r2= np.full((500, 500, 3), [0, 255, 255], dtype=np.uint8)

# print(r1)

cv2.imshow("Olusan resim1", r1)
cv2.imshow("Olusan resim2", r2)

cv2.waitKey(0)
 
cv2.destroyAllWindows()