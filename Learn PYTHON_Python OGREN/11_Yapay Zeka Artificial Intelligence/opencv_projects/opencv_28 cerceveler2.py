# cerceve
import cv2
import matplotlib.pyplot as plt
r1 = cv2.imread('images/ornekresim01_150x100.png')

c1 = cv2.copyMakeBorder(r1,10,10,10,10, cv2.BORDER_REPLICATE)
c2 = cv2.copyMakeBorder(r1,10,10,10,10, cv2.BORDER_REFLECT)
c3 = cv2.copyMakeBorder(r1,10,10,10,10, cv2.BORDER_REFLECT101)
c4 = cv2.copyMakeBorder(r1,10,10,10,10, cv2.BORDER_REFLECT_101)
c5 = cv2.copyMakeBorder(r1,10,10,10,10, cv2.BORDER_WRAP)
c6 = cv2.copyMakeBorder(r1,10,10,10,10, cv2.BORDER_DEFAULT)
c7 = cv2.copyMakeBorder(r1,10,10,10,10, cv2.BORDER_ISOLATED)
c8 = cv2.copyMakeBorder(r1,10,10,10,10, cv2.BORDER_CONSTANT, value=[255,0,255])

plt.subplot(2,5,1), plt.imshow(r1), plt.title('Orjinal')
plt.subplot(2,5,2), plt.imshow(c1), plt.title('REPLICATE')
plt.subplot(253), plt.imshow(c2), plt.title('REFLECT')
plt.subplot(254), plt.imshow(c3), plt.title('REFLECT101')
plt.subplot(255), plt.imshow(c4), plt.title('REFLECT_101')
plt.subplot(257), plt.imshow(c5), plt.title('WRAP')
plt.subplot(258), plt.imshow(c6), plt.title('DEFAULT')
plt.subplot(259), plt.imshow(c7), plt.title('ISOLATED')
plt.subplot(2,5,10), plt.imshow(c8), plt.title('CONSTANT')

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()