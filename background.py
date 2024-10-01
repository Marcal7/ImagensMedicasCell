import numpy as np
import cv2
import matplotlib.pyplot as plt
from rembg import remove
from PIL import Image

# Variáveis das fotos
img_path = 'cel.tif'  # Caminho da sua imagem
img_output = 'processed_image.tif'  # Caminho para a imagem de saída

input_image = Image.open(img_path)
output_image = remove(input_image)
output_image.save(img_output)

# Carregar a imagem processada sem fundo
imagem = cv2.imread(img_output)

# Converter a imagem para o espaço de cor HSV
hsv_image = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)

# Ajustar limites para a cor
lower = np.array([15, 20, 20])  # Limite inferior ajustado
upper = np.array([30, 255, 255])  # Limite superior ajustado

# Criar a máscara para os biomarcadores marrons
mask = cv2.inRange(hsv_image, lower, upper)
img = cv2.bitwise_and(hsv_image, hsv_image, mask=mask)

height, width = img.shape[:2]
max_height = 800  # Altura máxima permitida
max_width = 800  # Largura máxima permitida

# Verificar se a imagem precisa ser redimensionada
if height > max_height or width > max_width:
    scaling_factor = min(max_height / float(height), max_width / float(width))
    img_resized = cv2.resize(img, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)
else:
    img_resized = img

# Verificar se a máscara precisa ser redimensionada
if height > max_height or width > max_width:
    scaling_factor = min(max_height / float(height), max_width / float(width))
    mask_resized = cv2.resize(mask, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)
else:
    mask_resized = mask

# Encontrar contornos na máscara redimensionada
contours, _ = cv2.findContours(mask_resized, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Contar o número de contornos (pontos distintos)
num_points = len(contours)

print(f'Número de pontos marrons encontrados: {num_points}')

# Mostrar a máscara redimensionada
cv2.imshow('Máscara Redimensionada', mask_resized)
cv2.waitKey(0)

# Mostrar a imagem redimensionada
cv2.imshow('Imagem Redimensionada', img_resized)
cv2.waitKey(0)

# --------------------------------------

# Converter para escala de cinza
gray_img = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# Fazer algum processamento em escala de cinza, como detecção de bordas
edges = cv2.Canny(gray_img, 100, 200)

# Verificar se a imagem precisa ser redimensionada
if height > max_height or width > max_width:
    scaling_factor = min(max_height / float(height), max_width / float(width))
    img_resized = cv2.resize(edges, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)
else:
    img_resized = edges

# Mostrar a imagem redimensionada
cv2.imshow('Imagem Redimensionada', img_resized)
cv2.waitKey(0)

print('finalizado')
exit()
