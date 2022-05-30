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

## СДВИГАЕМ / ПЕРЕВОДИМ
# если отрицательный X, то сдвигаем влево
# если отрицательный Y, то сдвигаем вверх
# если положительный X, то сдвигаем вправо
# если положительный Y, то сдвигаем вниз
def translateImage(img, x, y):
    # x, y  - в пикселях
    transMatrix = np.float32([[1, 0, x], [0, 1, y]])
    # dim = (width, height)
    dim = (img.shape[1], img.shape[0])
    return cv2.warpAffine(img, transMatrix, dim)

# tr1 = translateImage(image, 100, 100)
# cv2.imshow('tr100', tr1)
#
# tr2 = translateImage(image, -100, -50)
# cv2.imshow('tr-100', tr2)

### ВРАЩЕНИЕ
def rotateImage(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    if rotPoint is None: # значит, что  пращение вокруг центра
        rotPoint = (width // 2, height // 2)
    #    : центр точки поворота, угол поворота, масштаб (без масштаба= 1.0)
    rotMatrix = cv2.getRotationMatrix2D(rotPoint, angle, 1.0)
    dim = (width, height)
    return cv2.warpAffine(img, rotMatrix, dim)

# rot = rotateImage(image, 45) # против часовой
# cv2.imshow('rot1', rot)

# rot = rotateImage(image, -40) # по часовой
# cv2.imshow('rot2', rot)

# rot = rotateImage(rot, -45) # ЕЩЕ по часовой, есть скошенные линии
# cv2.imshow('rot 3 ', rot)

### ПЕРЕВОРОТ
# flipCode = 0   - по вертикале (низ это верх, верх это низ)
# flipCode =  1  - по горизонтале (право это лево, лево это право)
# flipCode = -1  - и по горизонтале и по вертикале
flip = cv2.flip(image, 0)
cv2.imshow('flip', flip)

## НАРЕЗКА
#             [  n   ,  m  ]
cropped = image[50:200, 200:400]
cv2.imshow('cropped ', cropped)




#python transformations.py
cv2.waitKeyEx(0)