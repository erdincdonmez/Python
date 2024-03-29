# boş resim oluşturma
import cv2
import numpy as np

# aşağıdaki [255, 255, 255] rakamlarını oynayarak ne olduğuna bakın
r1= np.full((500, 500, 3), [255, 255, 255], dtype=np.uint8)

cv2.imshow("Olusan resim", r1)

cv2.waitKey(0)
 
cv2.destroyAllWindows()


