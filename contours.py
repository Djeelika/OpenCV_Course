import cv2
import numpy as np

def rescaleImage(frame, scale = 0.5):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)

image = cv2.imread('Photos/Dexter1.jpg')
image = rescaleImage(image, 0.3) # оставили 30%, уменьшили размер на 70%
cv2.imshow('Dex', image)

###### ------  КОНТУРЫ - границы объектов -------

## Оттенки серого
# grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.imshow('grey', grey)

## ПОИСК разниц градиентов
# 50 и 150 - пороговые значения разницы градиентов
# canny_image = cv2.Canny(image, 125, 175)
# cv2.imshow('canny', canny_image)

# Получам КОНТУРЫ и высокие ключи
# cv2.RETR_EXTERNAL - извлекает только крайние внешние контуры.
# Он задает все контуры. hierarchy[i][2]=hierarchy[i][3]=-1
# cv2.RETR_LIST - извлекает все контуры без установления иерархических связей.
# cv2.RETR_TREE - извлекает все контуры и реконструирует полную иерархию вложенных контуров.
# cv2.RETR_CCOMP - извлекает все контуры и организует их в двухуровневую иерархию.
# На верхнем уровне находятся внешние границы компонентов.
# На втором уровне есть границы отверстий. Если внутри отверстия
# соединяемого компонента есть еще один контур, его все равно ставят на верхний уровень.
# УКАЗЫВАЕМ алгоритм приближения контура
# cv2.CHAIN_APPROX_NONE - хранит абсолютно все контурные точки, то есть max(abs(x1-x2),abs(y2-y1))==1.
# cv2.CHAIN_APPROX_SIMPLE - сжимает горизонтальные, вертикальные и диагональные сегменты и оставляет только их конечные точки.

# contours, hierarchy = cv2.findContours(canny_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# print(len(contours))           # 623 нашлось контуров. СПИСОК СПИСКОВ
# print(len(contours[0]))        # 11
# print(len(contours[524]))      # 64
# print(len(contours[524][45]))  # 1
# print(contours[0])

### Пробуем После РАЗМЫТИЯ
# grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# blur = cv2.GaussianBlur(grey , (5,5), cv2.BORDER_DEFAULT)
# cv2.imshow('blur', blur)
# canny_blur = cv2.Canny(blur, 125, 175)
# cv2.imshow('canny blur', canny_blur)
# contours, hierarchy = cv2.findContours(canny_blur, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
#
# print(len(contours))           # 72 нашлось контуров. СПИСОК СПИСКОВ
# print(len(contours[0]))        # 26

# ------------------------------
### Пробуем ч/з Пороговое значение
# grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#
# # ниже порога установим значение 0, выше порога значение maxval
# #                        : на чем, порог, maxval, тип пороговых значений
# ret, thresh = cv2.threshold(grey, 125, 255, cv2.THRESH_BINARY)
# cv2.imshow('thresh', thresh)
# contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# print(len(contours))           # 146 нашлось контуров. СПИСОК СПИСКОВ
# print(len(contours[0]))        # 1

# ------------------------------
### РИСУЕМ КОНТУРЫ на Пустом Бланке
## blank = np.zeros((image.shape[0], image.shape[1], 3), dtype='uint8')
# blank = np.zeros(image.shape, dtype='uint8')
# # на чем, контуры, индексы нужных контуров (если все контуры = -1), цвет, толщена
# cv2.drawContours(blank, contours, -1, (0, 150, 0), 1)
# cv2.imshow('blank', blank)


# ------------------------------
### РИСУЕМ КОНТУРЫ ч/з  Canny
canny_image = cv2.Canny(image, 125, 175)
cv2.imshow('canny', canny_image)

contours, hierarchy = cv2.findContours(canny_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# blank = np.zeros(image.shape, dtype='uint8')
# cv2.drawContours(blank, contours, -1, (0, 150, 0), 1)
# cv2.imshow('blank', blank)


## наложение на основное фото
cv2.drawContours(image, contours, -1, (0, 150, 0), 1)
cv2.imshow('imageContours', image)


cv2.waitKeyEx(0)