import cv2
import numpy as np
import matplotlib.pyplot as plt

# -----------   ПОБИТОВЫЕ ОПЕРАЦИИ  -------------------
blank = np.zeros((400, 400), dtype='uint8')

# Рисуем Прямоугольник
# подаем начальную точку(30, 30), конечную(370, 370), Цвет (255), толщену(закрасить -1)
rectingle = cv2.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
#    подаем центр(200, 200), радиус(200),Цвет (255),толщену(закрасить -1)
circle = cv2.circle(blank.copy(), (200, 200), 200, 255, -1)

cv2.imshow('rectingle', rectingle)
cv2.imshow('circle', circle)

#  УМНОЖЕНИЕ ___  ПРЯМОУГОЛЬНИК и КРУГ
# Пересечение. Закрашено только то, что есть в ОБОИХ
bitwise_and = cv2.bitwise_and(rectingle, circle)
cv2.imshow('bitwise_and', bitwise_and)

#  СЛОЖЕНИЕ ___  ПРЯМОУГОЛЬНИК и КРУГ
# Закрашено то, что есть в Прямоугольнике или в Квадрате
bitwise_or = cv2.bitwise_or(rectingle, circle)
cv2.imshow('bitwise_or', bitwise_or)

#  Исключающее СЛОЖЕНИЕ  ___  ПРЯМОУГОЛЬНИК и КРУГ
# Закрашено то, что есть ИЛИ в Прямоугольнике ИЛИ в Квадрате, но не в обоих.
bitwise_xor = cv2.bitwise_xor(rectingle, circle)
cv2.imshow('bitwise_or', bitwise_xor)



#  ОТРИЦАНИЕ ___  ПРЯМОУГОЛЬНИК и КРУГ
# Закрашено пустые места, т.е. инвертировали побитовый.
bitwise_not = cv2.bitwise_not(circle)
cv2.imshow('bitwise__not', bitwise_not)


cv2.waitKeyEx(0)