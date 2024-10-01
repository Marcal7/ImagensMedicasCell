from rembg import remove
from PIL import Image

img_path = ''  # Caminho da sua imagem
img_output = ''

input_image = Image.open(img_path)
output_image = remove(input_image)
output_image.save(img_output)
