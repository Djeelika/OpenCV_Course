import cv2
import numpy as np
import matplotlib.pyplot as plt

def rescaleImage(frame, scale = 0.5):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)

image = cv2.imread('Photos/Dexter2.jpg')
image = rescaleImage(image, 0.3) # оставили 30%, уменьшили размер на 70%
cv2.imshow('Dex', image) # отобразилось как RGB (правильно)
# plt.imshow(image)      # отобразилось как BGR (НЕ правильно)
# plt.show()

# ---------- ВЫЧИСЛЯЕМ Гистограмму  для Серого -------------------
# # Оттенки серого
# grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #
# cv2.imshow('grey', grey)

# #  для серого только один канал =0, maska=None, размер, диапазон=[0, 256]
# grey_hist = cv2.calcHist([grey], [0], None, [256], [0, 256])
# plt.figure()
# plt.title('grey_histogram')
# plt.xlabel('Bins')             # интервалы интенсивности
# plt.ylabel('# of pixels')      # количество Пикселей в определенной интенсивности
# plt.plot(grey_hist)
# plt.xlim([0, 256]) # Ограничение по оси Х
# plt.show()
# # Получили График интенсивности Пикселей



# ---------- ВЫЧИСЛЯЕМ Гистограмму по Маске ----------------

# blank = np.zeros(image.shape[:2], dtype='uint8')
# cv2.imshow('blank image', blank)

# готовим Маску: на чистом бланке, центр(центр image), радиус(200), цвет(255),толщену(закрасить -1)
# mask_circle = cv2.circle(blank.copy(), (image.shape[1]//2, image.shape[0]//2), 200, 255, -1)
# cv2.imshow('mask image', mask)

# # --- Замаскерованное Серое
# # ПЕРЕСЕЧЕНИЕ (Побитовое Умножение)
# masked_image = cv2.bitwise_and(grey, grey, mask=mask_circle)
# cv2.imshow('masked_image', masked_image)

# #  для серого только один канал =0, maska, размер, диапазон=[0, 256]
# grey_hist = cv2.calcHist([grey], [0], masked_image, [256], [0, 256])
#
# plt.figure()
# plt.title('grey_histogram')
# plt.xlabel('Bins')             # интервалы интенсивности
# plt.ylabel('# of pixels')      # количество Пикселей в определенной интенсивности
# plt.plot(grey_hist)
# plt.xlim([0, 256])   # Ограничение по оси Х
# plt.show()
# # Получили График интенсивности Пикселей по Маске
# # --------------------------

# ---------- ВЫЧИСЛЯЕМ Гистограмму для Цветного ----------------

blank = np.zeros(image.shape[:2], dtype='uint8')

# готовим Маску: на чистом бланке, центр(центр image), радиус(200), цвет(255),толщену(закрасить -1)
mask_circle = cv2.circle(blank.copy(), (image.shape[1]//2, image.shape[0]//2), 200, 255, -1)
# cv2.imshow('mask image', mask_circle)

# --- Замаскерованное Серое
# ПЕРЕСЕЧЕНИЕ (Побитовое Умножение)
masked_image = cv2.bitwise_and(image, image, mask=mask_circle)
cv2.imshow('masked_image', masked_image)


plt.figure()
plt.title('Color_MASKA')
plt.xlabel('Bins')             # интервалы интенсивности
plt.ylabel('# of pixels')      # количество Пикселей в определенной интенсивности
color = ('b', 'g', 'r')
for i, col in enumerate(color):
    hist = cv2.calcHist([image], [i], mask_circle, [256], [0, 256])
    plt.plot(hist, color= col)
    plt.xlim([0, 256])  # Ограничение по оси Х
plt.show()


plt.figure()
plt.title('Color_histogram')
plt.xlabel('Bins')             # интервалы интенсивности
plt.ylabel('# of pixels')      # количество Пикселей в определенной интенсивности
color = ('b', 'g', 'r')
for i, col in enumerate(color):
    hist = cv2.calcHist([image], [i], None, [256], [0, 256])
    plt.plot(hist, color= col)
    plt.xlim([0, 256])  # Ограничение по оси Х
plt.show()
# Получили График интенсивности Пикселей Всех цветов



cv2.waitKeyEx(0)