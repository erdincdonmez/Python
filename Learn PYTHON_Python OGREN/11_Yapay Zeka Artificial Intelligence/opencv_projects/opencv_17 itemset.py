# Temel resim işlemleri
import cv2

img1 = cv2.imread('images/ornekresim01_150x100.png')

print(img1) # tüm pixellerin içi özet olarak
print("Resimdeki satır sayısı: ",len(img1)) # satır

for a in range(len(img1)):
    print(a, img1[a][0])

for a in range(len(img1)-1):
    img1.itemset((a,a,0),0)
    # img1.itemset((a+1,a,0),0)
    img1.itemset((a,a,1),0)
    # img1.itemset((a+1,a,1),0)
    img1.itemset((a,a,2),0)
    # img1.itemset((a+1,a,2),0)
    print(a, img1[a][0])

cv2.imshow('değişiklik',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()