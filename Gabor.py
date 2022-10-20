import cv2
import matplotlib.pyplot as plt

# Ksize 是一个元组
retval = cv2.getGaborKernel(ksize=(111,111), sigma=10, theta=60, lambd=10, gamma=1.2)
image1 = cv2.imread('./pictures/nvwa.jpg')
result = cv2.filter2D(image1,-1,retval)

plt.figure(figsize=(10,14))

plt.subplot(221)
plt.imshow(image1, cmap='gray')
plt.title('Origin')

plt.subplot(222)
plt.imshow(result, cmap='gray')
plt.title('Gabor')

plt.show()


#cv2.imshow('result',result)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

