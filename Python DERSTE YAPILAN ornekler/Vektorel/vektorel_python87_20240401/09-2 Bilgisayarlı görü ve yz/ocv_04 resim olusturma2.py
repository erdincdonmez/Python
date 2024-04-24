# resim1 = ([[250],[200],[150],[100]]) # gri tonlarda 4 pixellik bir resim olabilir.
# resim2 = [
    # [250,200,150,100],
    # [250,200,150,100],
    # [250,200,150,100],
    # ] # gri tonları 4x3 pixellik bir resim olabilir.
# resim3 = [[250,0,0],[200,0,0],[150,0,0],[100,0,0]] # kırmızı tonlarda RGB 4 pixellik bir resim olabilir.

# resim4 = [
#     [[250,0,0],[200,0,0],[150,0,0],[100,0,0]],
#     [[250,0,0],[200,0,0],[150,0,0],[100,0,0]],
#     [[250,0,0],[200,0,0],[150,0,0],[100,0,0]]
#     ] # kırmızı tonlarda RGB 12 pixellik bir resim olabilir.

# pip install numpy
import numpy as np
resim5= np.full((300, 500, 3), [255, 0, 0], dtype=np.uint8)
resim6= np.full((5, 7, 3), [100, 0, 100], dtype=np.uint8)
resim7= np.full((5, 7, 1), [150], dtype=np.uint8)
resim8= np.full((5, 7, 1), [50], dtype=np.uint8)
# print(resim7)

import cv2
# img = cv2.imread('images/bayrak1.png')
cv2.namedWindow("Deneme1", cv2.WINDOW_NORMAL)
cv2.namedWindow("Deneme2", cv2.WINDOW_NORMAL)
cv2.imshow('Deneme1',resim7)
cv2.imshow('Deneme2',resim8)
cv2.waitKey(0) # 3 saniye bekle
cv2.destroyAllWindows() # pencereleri kapa

# pip install opencv-python
# import cv2
# print(cv2.__version__)
