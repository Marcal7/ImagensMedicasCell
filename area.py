import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from random import randint # vamos utilizar cores aleatórias para exibir os contornos da imagem


# Carrega a imagem
im = cv.imread('processed_image.tif')

print('Largura da imagem:', im.shape[1])
print('Altura da imagem:', im.shape[0])
print('\n')

imgray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)

# Aplica o desfoque
print('Desfoque...')
blur = cv.blur(imgray, (15, 15))

# Aplica o threshold (limite)
print('Limite...')
ret, thresh = cv.threshold(blur, 10, 255, cv.THRESH_BINARY)

# Encontra os contornos
print('Contorno...')
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

# Cria uma máscara preta do mesmo tamanho da imagem original
mask = np.zeros(im.shape[:2], dtype=np.uint8)

# Preenche a máscara com os contornos
cv.drawContours(mask, contours, -1, (255), thickness=cv.FILLED)

# Conta o número de pixels brancos (valor 255) na máscara
pixel_count = cv.countNonZero(mask)
print('\n')
print(f'Número de pixels dentro das áreas delimitadas pelos contornos: {pixel_count}')

# Visual
img_contour = im.copy()

# Desenha todos os contornos na cópia da imagem
for i, c in enumerate(contours):
    cv.drawContours(img_contour, contours, i, (randint(0, 255), randint(0, 255), randint(0, 255)), 3)

# Exibe a imagem com contornos desenhados
plt.imshow(cv.cvtColor(img_contour, cv.COLOR_BGR2RGB))
plt.title('Com Contornos')
plt.show()