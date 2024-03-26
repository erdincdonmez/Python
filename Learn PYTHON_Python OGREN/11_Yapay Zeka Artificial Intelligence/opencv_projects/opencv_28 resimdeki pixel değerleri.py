import cv2

r = cv2.imread("images/ornekresim01_600x400.png")

print("\nTüm resim dizisi:\n", r)
print("\nBir parça (r[50,50]): ",r[50,50]) # img[x,y]
print("\nBir parça (r[2:5,1:3]):\n",r[2:5,1:3]) # img[y1:y2, x1:x2]