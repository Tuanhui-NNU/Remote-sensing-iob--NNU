import cv2
import numpy as np
import matplotlib.pyplot as plt

def Laplace(img, kernel):

    des_8U = cv2.filter2D(img, -1, kernel=kernel, borderType=cv2.BORDER_DEFAULT)
    des_16S = cv2.filter2D(img, ddepth=cv2.CV_16SC1, kernel=kernel, borderType=cv2.BORDER_DEFAULT)

    g = img - des_16S
    g[g<0] = 0
    g[g>255] = 255

    plt.figure(figsize=(10,14))

    # origin, Undecided, Calibrate, Filtered
    plt.subplot(221)
    plt.imshow(img, cmap='gray')
    plt.title('Origin')

    plt.subplot(222)
    plt.imshow(des_8U, cmap='gray')
    plt.title('Undecided')

    plt.subplot(223)
    plt.imshow(des_16S, cmap='gray')
    plt.title('Calibrate')

    plt.subplot(224)
    plt.imshow(g, cmap='gray')
    plt.title('Filtered')
    plt.show()

img0 = './pictures/flower.jpg'

f = cv2.imread(img0, cv2.IMREAD_GRAYSCALE)

kernel1 = np.asarray([[0, 1, 0],
                      [1, -4, 1],
                      [0, 1, 0]])

Laplace(f, kernel1)

