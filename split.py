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

b, g, r = cv2.split(image)
# cv2.imshow('blue', b)  # в оттенках серого концентрация Синего канала
# cv2.imshow('green', g) # в оттенках серого концентрация Зеленого канала
# cv2.imshow('red', r)   # в оттенках серого концентрация Красного канала
# print(image.shape)  # (369, 657, 3)
# print(b.shape)      #(369, 657)
# print(g.shape)      #(369, 657)
# print(r.shape)      #(369, 657)
#
# # СЛИЯНИЕ трех каналов
# merge = cv2.merge([b, g, r])
# cv2.imshow('merge', merge)

# ----------------------------------
blank = np.zeros(image.shape[:2], dtype='uint8')

blank_b = cv2.merge([b, blank, blank])
blank_g = cv2.merge([blank, g, blank])
blank_r = cv2.merge([blank, blank, r])

cv2.imshow('blue', blank_b)  # фото в оттенках Синего цвета
cv2.imshow('green', blank_g) # фото в оттенках Зеленого цвета
cv2.imshow('red', blank_r)   # фото в оттенках Красного цвета

print(blank_b.shape)      #(369, 657, 3)
print(blank_g.shape)      #(369, 657, 3)
print(blank_r.shape)      #(369, 657, 3)




cv2.waitKeyEx(0)