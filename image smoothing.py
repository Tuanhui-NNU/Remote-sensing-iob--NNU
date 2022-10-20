import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('./pictures/TowerNoise.jpg', 0)
h = img.shape[0]
w = img.shape[1]

# 均值滤波
img_Blur_5 = cv.blur(img, (5, 5))   # 5*5均值滤波

# 中值滤波
img_MedianBlur_5 = cv.medianBlur(img, 5)    # 5*5中值滤波

# 超限像素平滑法
def overrun_pixel_smoothing(kernel, image):
    img_overrun = image.copy()
    filter = np.zeros((kernel, kernel), np.uint8)
    average = np.zeros((h - kernel + 1, w - kernel + 1), np.uint8)  # 平均值矩阵

    for i in range(h - kernel + 1):
        for j in range(w - kernel + 1):

            for m in range(kernel):
                for n in range(kernel):
                    filter[m, n] = img_overrun[i + m, j + n]

            average[i, j] = 1 / (kernel * kernel) * filter.sum()  # 求平均

    T = 30  # 设定阈值

    for i in range(h - kernel + 1):
        for j in range(w - kernel + 1):

            if abs(img[i + kernel - 2, j + kernel - 2] - average[i, j]) > T:
                img_overrun[i + kernel - 2, j + kernel - 2] = average[i, j]

    return img_overrun

img_overrun_5 = overrun_pixel_smoothing(5, img)  # 核大小为5*5

plt.figure(figsize=(10,14))

# origin, Mean, Median, Over-limit pixel
plt.subplot(221)
plt.imshow(img, cmap='gray')
plt.title('Origin')

plt.subplot(222)
plt.imshow(img_Blur_5, cmap='gray')
plt.title('Mean')

plt.subplot(223)
plt.imshow(img_MedianBlur_5, cmap='gray')
plt.title('Median')

plt.subplot(224)
plt.imshow(img_overrun_5, cmap='gray')
plt.title('Over-limit pixel')
plt.show()


