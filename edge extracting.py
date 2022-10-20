import cv2
import matplotlib.pyplot as plt

# 1.转化为灰度图
img = cv2.imread('./pictures/nvwa.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 2.高斯模糊
gaussian = cv2.GaussianBlur(gray, (5, 5), 6)
# 3.Canny边缘提取
canny = cv2.Canny(gaussian, 50, 150)


plt.figure(figsize=(10,14))

plt.subplot(231)
plt.imshow(img, cmap='gray')
plt.title('Origin')

plt.subplot(232)
plt.imshow(gaussian, cmap='gray')
plt.title('Gaussian')

plt.subplot(233)
plt.imshow(canny, cmap='gray')
plt.title('Canny')
plt.show()

