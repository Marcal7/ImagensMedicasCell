import area
import contagem
import tirarfundo

# ----------

import os
import pandas as pd

pasta = input("Diretório da pasta: ")
arquivos = os.listdir(pasta)

extensoes_validas = {".png", ".jpg", ".jpeg", ".tif"}

dados = []

for index, file in enumerate(arquivos):
    caminho = os.path.join(pasta, file)
    extensao = os.path.splitext(file)[1].lower()

    if extensao in extensoes_validas:
        tirarfundo.remove_background(caminho, pasta, index)

        image_output = os.path.join(pasta, f"output{index}.tif")

        pixel_count = area.calc_area(image_output)

        azul, marrom = contagem.pontos(image_output)

        dados.append({
            "Index": index,
            "Nome do Arquivo": file,
            "Área": pixel_count,
            "Biomarcadores Azuis": azul,
            "Biomarcadores Marrons": marrom
        })

    else:
        print(f"Arquivo {file} ignorado")

df = pd.DataFrame(dados)
df.to_excel("resultado.xlsx", index=False)
print("Dados salvos")