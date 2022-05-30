import cv2
import numpy as np
import matplotlib.pyplot as plt

def rescaleImage(frame, scale = 0.5):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)

image = cv2.imread('Photos/Dexter1.jpg')
image = rescaleImage(image, 0.3) # оставили 30%, уменьшили размер на 70%
cv2.imshow('Dex', image) # отобразилось как RGB (правильно)
# plt.imshow(image)      # отобразилось как BGR (НЕ правильно)
# plt.show()

blank = np.zeros(image.shape[:2], dtype='uint8')
# cv2.imshow('blank image', blank)
# --------------------------

# готовим Маску: на чистом бланке, центр(центр image), радиус(200), цвет(255),толщену(закрасить -1)
mask = cv2.circle(blank.copy(), (image.shape[1]//2, image.shape[0]//2), 200, 255, -1)
cv2.imshow('mask image', mask)


# --------- Замаскерованное Изображение  -------------
# ПЕРЕСЕЧЕНИЕ (Побитовое Умножение)
masked_image = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow('masked_image', masked_image)



cv2.waitKeyEx(0)