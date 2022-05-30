import cv2
#from google.colab.patches import cv2_imshow   # вместо cv2.imshow в КОЛАБЕ !!!
import numpy as np

def rescaleImage(frame, scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)


Image= cv2.imread('Dexter1.jpg')
# Меняем размер
# Image = cv2.resize(Image, (900, 500), interpolation=cv2.INTER_AREA)
img = rescaleImage(Image, 0.5)
cv2.imshow('Dex', img)

#Переведём изображение в другую палитру
#img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # НЕ НУЖНО здесь !!!
#cv2.imshow('Dex', img)


# Пустой бланк
blank = np.zeros((img.shape[0], img.shape[1], 3), dtype='uint8')
#cv2.imshow('blank', blank)

#blank[:] = 0,255,0
#cv2.imshow('green', blank)

#blank[:] = 0,0,255
#cv2.imshow('RED', blank)

# [ n , m ]
#blank[200:300] = 0,0,255            # горизонтальная полоса
#blank[:, 200:300] = 0,0,255         # вертикальная полоса
#blank[400:450, 200:300] = 0,0,255

# ПРЯМОУГОЛЬНИК: на чем рисуем, (x1,y1), (x2,y2), цвет, толщена границ =2 или заполнение(-1)
#cv2.rectangle(blank, (0, 10), (400, 200), (100, 150, 0), thickness=cv2.FILLED)
#cv2.rectangle(img, (0, 10), (400, 200), (100, 150, 0), thickness=2)
#cv2.rectangle(blank, (0, 0), (blank.shape[1]//2, blank.shape[0]//2), (100, 150, 0), thickness=-1)
#cv2.imshow('kvadrat', img)

# КРУГ: на чем рисуем, центр(x,y), радиус, цвет, толщена
#cv2.circle(blank, (250, 250), 40, (50, 50, 0), thickness=-1)
#cv2.imshow('Круг', blank)

# Рисуем линию: на чем рисуем, (x1,y1), (x2,y2), цвет, толщена границ
#cv2.line(blank, (0, 10), (250, 250), (150, 50, 0), thickness= 5)
#cv2.imshow('Линия', blank)

## НАПИСАТЬ Текст: на чем, text, (x,y), Шрифт, масштаб шрифта, цвет, толщена границ
text = 'Безопасно'
cv2.putText(blank, text, (0, 450), cv2.FONT_HERSHEY_COMPLEX, 1.0, (0, 250, 150), 3)
cv2.imshow('Текст', blank)

### На ФОТО  НЕ рисует putText!!!
# text = 'Безопасно'
# cv2.putText(img, text, (0, 450), cv2.FONT_HERSHEY_COMPLEX, 1.0, (0, 250, 150), 3)
# cv2.imshow('0', img)

### СОЕДИНЕНИЕ ФОТО и ТЕКСТА с одинаковым размером
img2 = np.copy(img)
img2 = cv2.addWeighted(img2, 1, blank, 1, 1) # Накладываем БЛАНК на исходное изображение
cv2.imshow('addWeighted', img2)




cv2.waitKeyEx(0)


