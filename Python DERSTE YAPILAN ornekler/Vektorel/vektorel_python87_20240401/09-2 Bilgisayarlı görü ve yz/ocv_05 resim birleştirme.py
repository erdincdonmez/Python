# resim1 = ([[250],[200],[150],[100]]) # gri tonlarda 4 pixellik bir resim olabilir.

# pip install numpy
import numpy as np
resim5= np.full((100, 200, 3), [255, 0, 0], dtype=np.uint8)
resim6= np.full((100, 200, 3), [100, 0, 100], dtype=np.uint8)
resim7= np.full((100, 200, 1), [150], dtype=np.uint8)
resim8= np.full((100, 200, 1), [50], dtype=np.uint8)
arr6 = np.concatenate((resim5, resim6))
print(resim5)
print(resim6)

import cv2
# img = cv2.imread('images/bayrak1.png')
cv2.namedWindow("Deneme1", cv2.WINDOW_NORMAL)
cv2.imshow('Deneme1',arr6)
cv2.waitKey(0) # 3 saniye bekle
cv2.destroyAllWindows() # pencereleri kapa

