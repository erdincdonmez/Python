# https://medium.com/@volkan_aktas/opencv-i%CC%87le-resim-ve-video-g%C3%B6r%C3%BCnt%C3%BCleme-yazma-kaydetme-bc894e40f9fd
# https://bayramadali.wordpress.com/python-opencv-resim-okuma-ve-gosterme-islemlerine-giris/
# OpenCV kütüphanesini aşağıdaki komutlar ile yükle.
# pip install opencv-python

import cv2
img = cv2.imread ("denemeresim.jpg", 1 )
cv2.imshow ("image", img )
cv2.waitKey (0)
cv2.destroyAllWindows ()
