import cv2
import numpy as np

# aşağıdaki [255, 255, 255] rakamlarını oynayarak ne olduğuna bakın
r1= np.full((200, 300, 3), [255, 0, 255], dtype=np.uint8)
r2= np.full((200, 300, 3), [0, 255, 255], dtype=np.uint8)
r3 = np.concatenate((r1, r2))
# r4 = np.stack((r1, r2))
# print(r1)

# r5 = np.transpose(r3)

cv2.imshow("Olusan resim1", r1)
cv2.imshow("Olusan resim2", r2)
cv2.imshow("Olusan resim3", r3)
# cv2.imshow("Olusan resim4", r4)
# cv2.imshow("Olusan resim5", r5)
np.save("deneme",r3)
cv2.waitKey(0)
 
cv2.destroyAllWindows()