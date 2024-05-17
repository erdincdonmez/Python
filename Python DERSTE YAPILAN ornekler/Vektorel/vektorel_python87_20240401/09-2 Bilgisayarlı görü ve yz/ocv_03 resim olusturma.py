resim1 = [250,200,150,100] # gri tonlarda 4 pixellik bir resim olabilir.
resim21 = ([12, 11,  2,  9])
resim2 = ([
    [250,200,150,100],
    [250,200,150,100],
    [250,200,150,100]
    ]) # gri tonları 4x3 pixellik bir resim olabilir.
resim3 = [[250,0,0],[200,0,0],[150,0,0],[100,0,0]] # kırmızı tonlarda RGB 4 pixellik bir resim olabilir.

resim4 = ([
    [[250,0,0],[200,0,0],[150,0,0],[100,0,0]],
    [[250,0,0],[200,0,0],[150,0,0],[100,0,0]],
    [[250,0,0],[200,0,0],[150,0,0],[100,0,0]],
    ]) # kırmızı tonlarda RGB 12 pixellik bir resim olabilir.

import cv2
# img = cv2.imread('images/bayrak1.png')
img = cv2.imread('resimler/sifreEkrani.PNG')
print(img)
cv2.imshow('Deneme',img)
# cv2.imshow('Deneme',resim1)
cv2.waitKey(3000) # 3 saniye bekle
cv2.destroyAllWindows() # pencereleri kapa

# pip install opencv-python
# import cv2
# print(cv2.__version__)
