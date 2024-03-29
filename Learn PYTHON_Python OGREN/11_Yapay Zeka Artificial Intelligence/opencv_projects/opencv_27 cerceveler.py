# cerceve
import cv2
r1 = cv2.imread('images/ornekresim01_150x100.png')

c1 = cv2.copyMakeBorder(r1,10,10,10,10, cv2.BORDER_REPLICATE)
c2 = cv2.copyMakeBorder(r1,10,10,10,10, cv2.BORDER_REFLECT)
c3 = cv2.copyMakeBorder(r1,10,10,10,10, cv2.BORDER_REFLECT101)
c4 = cv2.copyMakeBorder(r1,10,10,10,10, cv2.BORDER_REFLECT_101)
c5 = cv2.copyMakeBorder(r1,10,10,10,10, cv2.BORDER_WRAP)
c6 = cv2.copyMakeBorder(r1,10,10,10,10, cv2.BORDER_DEFAULT)
c7 = cv2.copyMakeBorder(r1,10,10,10,10, cv2.BORDER_ISOLATED)
c8 = cv2.copyMakeBorder(r1,10,10,10,10, cv2.BORDER_CONSTANT, value=[255,0,255])

cv2.imshow('BORDER_REPLICATE            ',c1)
cv2.imshow('BORDER_REFLECT              ',c2)
cv2.imshow('BORDER_REFLECT101           ',c3)
cv2.imshow('BORDER_REFLECT_101          ',c4)
cv2.imshow('BORDER_WRAP                 ',c5)
cv2.imshow('BORDER_DEFAULT              ',c6)
cv2.imshow('BORDER_ISOLATED             ',c7)
cv2.imshow('BORDER_CONSTANT, [0,255,0]  ',c8)
cv2.waitKey(0)
cv2.destroyAllWindows()