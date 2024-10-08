import numpy as np
import cv2

def contagemazul(image):
    # Carregar a imagem processada sem fundo
    imagem = cv2.imread(image)

    # Converter a imagem para o espaço de cor HSV
    hsv_image = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)

    lower = np.array([(170, 30, 30)])
    upper = np.array([220, 255, 255])

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

    num_points_blue = len(contours)
    return num_points_blue


def contagemmarrom(image):
    # Carregar a imagem processada sem fundo
    imagem = cv2.imread(image)

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
    num_points_brown = len(contours)
    return num_points_brown

def pontos(image):
    azul = contagemazul(image)
    marrom = contagemmarrom(image)
    return azul, marrom