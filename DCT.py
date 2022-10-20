import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('./pictures/laozi.jpg', 0)

img1 = img.astype(np.float32)

img11 = cv2.dct(img1)

for i in range(0,240):
     for j in range(0,320):
         if i > 100 or j > 100:
             img11[i,j] = 0

img12 = cv2.idct(img11)

plt.figure(figsize=(10,14))

plt.subplot(231)
plt.imshow(img, cmap='gray')
plt.title('Origin')

plt.subplot(232)
plt.imshow(img11, cmap='gray')
plt.title('DCT')

plt.subplot(233)
plt.imshow(img12.astype(np.uint8), cmap='gray')
plt.title('IDCT')
plt.show()

#cv2.imshow("Origin",img)
#cv2.imshow("Dct",img11)
#cv2.imshow("iDCT",img12.astype(np.uint8))
#cv2.waitKey(0)

