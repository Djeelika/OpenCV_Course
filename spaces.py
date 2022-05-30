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


###### ------  ПРОСТРАНСТВО ЦВЕТОВ -------

# ## Оттенки серого
# grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.imshow('grey', grey)
#
# ## HSV
# hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) # кислотные цвета
# cv2.imshow('hsv', hsv)
#
# ## LAB  (L * a * b)
# lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB) # кислотные цвета
# cv2.imshow('lab ', lab )

# Переведём изображение в RGB
RGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
cv2.imshow('RGB', RGB) # отобразилось как BGR (НЕ правильно)
plt.imshow(RGB)        # отобразилось как RGB (правильно)
plt.show()


cv2.waitKeyEx(0)