from rembg import remove
from PIL import Image
import os

def remove_background(image, paste, index):
    img_path = image  # Caminho da sua imagem
    img_output = os.path.join(paste, f"output{index}.tif")

    input_image = Image.open(img_path)
    output_image = remove(input_image)
    output_image.save(img_output)
