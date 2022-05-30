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

# -------------Сглаживание и Размытие  -----------------------
# УСРЕДНЕНИЕ
# Новая Интенсивность пикселя - это среднее значение окружающих пикселей Ядра
# размер ядра, например (3,3) (не четное), чем больше, тем более размыто
# average = cv2.blur(image, (3,3))
# cv2.imshow('average', average)
# ----------------

# Размытие по Гауссу менее размывает чем cv2.blur
#                размер ядра (не четное), границы точки по умолчанию
# Gausblur = cv2.GaussianBlur(image, (3,3), cv2.BORDER_DEFAULT)
# cv2.imshow('Gausblur', Gausblur)
# ------------------

# Размытие ЛУЧШЕ, чем по Гауссу
# Находим Медиану окружающих пикселей
#    размер ядра = 3, значит (3,3) (не четное)
median = cv2.medianBlur(image, 3)
cv2.imshow('median', median)
# ------------------

# Двухсторонее, Самое АККУРАТНОЕ
# подаем Диаметр окресности, например, =5
# далее значение Сигмы - бОльшее количество цветов, например =20
# далее Пространство Сигмы - те что расположены далеко будут влиять, например=20
bil = cv2.bilateralFilter(image, 5, 20, 20)
cv2.imshow('bil', bil)

cv2.waitKeyEx(0)