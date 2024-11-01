import numpy as np
import cv2
import matplotlib.pyplot as plt
from cv2 import imshow


def contagem(image, lhue, lsaturation, lvalue, uhue, usaturation, uvalue, canny_low, canny_upper):
    # Carregar a imagem processada sem fundo
    imagem = cv2.imread(image)

    # Converter a imagem para o espaço de cor RBG
    rgb_image = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)

    # Ajustar limites para a cor
    lower = np.array([lhue, lsaturation, lvalue])  # Limite inferior ajustado
    upper = np.array([uhue, usaturation, uvalue])  # Limite superior ajustado

    # Criar a máscara para os biomarcadores marrons
    mask = cv2.inRange(rgb_image, lower, upper)
    img = cv2.bitwise_and(rgb_image, rgb_image, mask=mask)

    edges = cv2.Canny(img, canny_low, canny_upper, apertureSize=7, L2gradient=False)

    # Encontrar contornos na máscara redimensionada
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    contornos_filtrados = []

    for contour in contours:
        area = cv2.contourArea(contour)

        if 10 <= area <= 100:
            contornos_filtrados.append(contour)

    # Contar o número de contornos (pontos distintos)
    num_points_brown = len(contours)
    num_contornos = len(contornos_filtrados)

    return num_contornos


def n_pontos(img):
    filtrar_azul = contagem(img, 20, 20, 120, 129, 129, 255, 75, 100)
    filtrar_marrom = contagem(img, 105, 105, 50, 255, 255, 110, 75, 100)

    return filtrar_azul, filtrar_marrom

    '''print(f"Azul: {azul} //// Marrom: {marrom}")
    print(f"Azul : 9197 //// Marrom: 254")
    
    print(f"Azul filtrado : {filtrar_azul}")
    print(f"Marrom filtrado : {filtrar_marrom}")'''

'''imgs_array = [img_azul, img_marrom, canny_edgA, canny_edgM]
titlesArray = ['Azul', 'Marrom', 'CannyAzul', 'CannyMarrom']

showMultipleImages(imgs_array, titlesArray, (12, 8), 2, 2)
writeMultipleImages(imgs_array, titlesArray, name='canny')'''