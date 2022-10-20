import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('./pictures/tower.jpg')
h = img.shape[0]
w = img.shape[1]

# 将彩色图片转换为灰度图片
grayimage = np.zeros((h, w), np.uint8)
for i in range(h):
    for j in range(w):
        grayimage[i, j] = 0.11 * img[i, j, 0] + 0.59 * img[i, j, 1] + 0.3 * img[i, j, 2] # python中以B G R存储图像

# 添加椒盐噪声
noiseimage = grayimage.copy()
SNR = 0.95    # 信噪比
pixels = h * w   # 计算图像像素点个数
noise_num = int(pixels * (1 - SNR))  # 计算图像椒盐噪声点个数

for i in range(noise_num):
    randx = np.random.randint(1, h-1)  # 生成一个 1 至 h-1 之间的随机整数
    randy = np.random.randint(1, w-1)  # 生成一个 1 至 w-1 之间的随机整数
    if np.random.random() <= 0.5:      # np.random.random()生成一个 0 至 1 之间的浮点数
        noiseimage[randx, randy] = 0
    else:
        noiseimage[randx, randy] = 255

plt.figure(figsize=(10,14))

# origin, Mean, Median, Over-limit pixel
plt.subplot(231)
plt.imshow(img, cmap='gray')
plt.title('Origin')

plt.subplot(232)
plt.imshow(grayimage, cmap='gray')
plt.title('Gray Tower')

plt.subplot(233)
plt.imshow(noiseimage, cmap='gray')
plt.title('NoiseTower')
plt.show()

cv.imwrite("./pictures/TowerGray.jpg", grayimage)
cv.imwrite("./pictures/TowerNoise.jpg", noiseimage)

