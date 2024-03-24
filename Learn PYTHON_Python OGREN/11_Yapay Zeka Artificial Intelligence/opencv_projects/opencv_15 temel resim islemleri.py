# Temel resim işlemleri
import cv2
img1 = cv2.imread('images/square1.jpg')
img2 = cv2.imread('images/square1.jpg',0)

# item
x = 100
y = 100
print(f'{x}, {y} noktası Blue  : ', img1.item(x,y,0))
print(f'{x}, {y} noktası Green : ', img1.item(x,y,1))
print(f'{x}, {y} noktası Red   : ', img1.item(x,y,2))

print(f'\n{x}, {y} noktası : {img1[x, y]}')
print(f'{x}, {y} noktası Blue  : {img1[x, y][0]}')
print(f'{x}, {y} noktası Green : {img1[x, y][1]}')
print(f'{x}, {y} noktası Red   : {img1[x, y][2]}')

# itemset
# shape
# size
# datatype
# ROI
# renk filtresi