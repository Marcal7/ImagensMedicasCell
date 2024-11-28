import numpy as np
import cv2

def contagem(image, lred, lgreen, lblue, ured, ugreen, ublue, canny_low, canny_upper, sfotos, index, tipo):
    # Carregar a imagem processada sem fundo
    imagem = cv2.imread(image)
    if imagem is None:
        print(f"Erro ao carregar a imagem: {image}")
        return

    # Converter a imagem para o espaço de cor RBG
    rgb_image = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)

    # Ajustar limites para a cor
    lower = np.array([lred, lgreen, lblue])  # Limite inferior ajustado
    upper = np.array([ured, ugreen, ublue])  # Limite superior ajustado

    # Criar a máscara para os biomarcadores marrons
    mask = cv2.inRange(rgb_image, lower, upper)
    img = cv2.bitwise_and(rgb_image, rgb_image, mask=mask)

    edges = cv2.Canny(img, canny_low, canny_upper, apertureSize=7, L2gradient=False)

    # Encontrar contornos na máscara redimensionada
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    circulo = []

    for contour in contours:
        area = cv2.contourArea(contour)
        perimeter = cv2.arcLength(contour, True)

        if perimeter > 0:
            circularity = (4 * np.pi * area) / (perimeter ** 2)

            if 0.2 <= circularity <= 1.5 and 10 <= area <= 200:
                circulo.append(contour)

    # Contar o número de contornos (pontos distintos)
    #num_points = len(contours)
    num_contornos = len(circulo)

    if sfotos is True:
        img_filtrada = cv2.drawContours(np.copy(rgb_image), circulo, -1, (0, 255, 0), 1)  # Contornos em verde
        cv2.imwrite(f'pontos{tipo}_filtrados{index}.png', img_filtrada)

    return num_contornos

def n_pontos(img, sfotos, index):
    filtrar_azul = contagem(img, 0, 0, 120, 140, 140, 255, 75, 100, sfotos, index, tipo='azul')
    filtrar_marrom = contagem(img, 0, 0, 0, 255, 255, 110, 75, 100, sfotos, index, tipo='marrom')

    return filtrar_azul, filtrar_marrom

    '''print(f"Azul: {azul} //// Marrom: {marrom}")
    print(f"Azul : 9197 //// Marrom: 254")
    
    print(f"Azul filtrado : {filtrar_azul}")
    print(f"Marrom filtrado : {filtrar_marrom}")'''

'''imgs_array = [img_azul, img_marrom, canny_edgA, canny_edgM]
titlesArray = ['Azul', 'Marrom', 'CannyAzul', 'CannyMarrom']

showMultipleImages(imgs_array, titlesArray, (12, 8), 2, 2)
writeMultipleImages(imgs_array, titlesArray, name='canny')'''