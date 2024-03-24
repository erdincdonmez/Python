# Temel resim işlemleri-pixel değerlerini okuma
import cv2

img1 = cv2.imread('images/ornekresim01_150x100.png')

print(img1) # tüm pixellerin içi özet olarak
print("Resimdeki satır sayısı: ",len(img1)) # satır

for a in range(len(img1)):
    print(a, img1[a][0])

# veya pixel bilgisi aşağıdaki şekilde de alınabilir
x = y = 20
print(f'{x}, {y} noktası Blue  : ', img1.item(x,y,0))
print(f'{x}, {y} noktası Green : ', img1.item(x,y,1))
print(f'{x}, {y} noktası Red   : ', img1.item(x,y,2))
