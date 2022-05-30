import cv2
#from google.colab.patches import cv2_imshow   # вместо cv2.imshow в КОЛАБЕ !!!
import numpy as np

image = cv2.imread('Dexter1.jpg')
# Меняем размер
img = cv2.resize(image, (640, 360), interpolation=cv2.INTER_AREA)
cv2.imshow('Dex', img)

# def rescaleFrame(frame, scale = 0.75):
#     width = int(frame.shape[1] * scale)
#     height = int(frame.shape[0] * scale)
#     dim = (width, height)
#     return cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)

## Оттенки серого
#grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #
#cv2.imshow('grey', grey)

# Уменьшение шума, Размытие по Гауссу
# на чем рисуем, ядро (не четное), границы точки по умолчанию
blur = cv2.GaussianBlur(img, (3,3), cv2.BORDER_DEFAULT)
#cv2.imshow('blur', blur)

# blur = cv2.GaussianBlur(img, (7,7), cv2.BORDER_DEFAULT) #здесь больше размыло
# cv2.imshow('blur2', blur)

## ПОИСК разниц градиентов
# canny_image = cv2.Canny(img, 80, 175)  # 50 и 150 - пороговые значения разницы градиентов
# cv2.imshow('canny', canny_image)

# canny_blur = cv2.Canny(blur, 80, 175)
# cv2.imshow('canny_blur3', canny_blur)

# расширение: на чем, ядро (не четное), количество итераций
# чем больше итераций, тем светлее/ярче/толще границы
# dil = cv2.dilate(canny_image, (3,3), iterations=1)
# cv2.imshow('canny_dil', dil)

## РАЗМЫТИЕ: на чем, ядро (не четное), количество итераций
# отменили dil = cv2.dilate(canny_image, (3,3), iterations=1)
# erod = cv2.erode(dil, (3,3), iterations=1)
# cv2.imshow('canny_dil_erod ', erod)

## Изменение размера
# Игнорируем соотношение сторон
# resized = cv2.resize(image, (500,500))

# с Интерполяцией!!!
# cv2.INTER_AREA  - ресамплинг с использованием отношения области пикселей.
# cv2.INTER_NEAREST - интерполяция ближайшего соседа
# cv2.INTER_LINEAR  - билинейная интерполяция - для Увеличения
# cv.INTER_CUBIC - бикубическая интерполяция - для Увеличения
# resized = cv2.resize(image, (500,500), interpolation=cv2.INTER_AREA)
# cv2.imshow('resized  ', resized)

## НАРЕЗКА
#             [  n   ,  m  ]
cropped = img[50:200, 200:400]
cv2.imshow('cropped ', cropped)


cv2.waitKeyEx(0)