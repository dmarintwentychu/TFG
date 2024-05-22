from PIL import Image
import numpy as np

# Abrir la imagen
img = Image.open("fary.jpg")
resized_img = img.resize((64, 64))
resized_img.save("fary.jpg")
resized_img.resize((128,128),resample=0).save("fary_near_neighbour.jpg")
#resized_img.resize((128,128),resample=).save("fary_near_neighbour.jpg")

img = Image.open("fary.jpg")

# Convertir la imagen a un array de numpy
img_array = np.array(img)

# Obtener las dimensiones originales de la imagen
original_height, original_width, channels = img_array.shape

# Definir el padding
padding = 1

# Calcular las nuevas dimensiones de la imagen
new_width = original_width * (padding + 1)
new_height = original_height * (padding + 1)

# Crear una nueva imagen con el fondo blanco
new_image = Image.new("RGB", (new_width, new_height), "white")

# Copiar los píxeles de la imagen original a la nueva imagen con el padding
for y in range(original_height):
    for x in range(original_width):
        pixel = img.getpixel((x, y))
        new_image.putpixel((x * (padding + 1), y * (padding + 1)), pixel)

# Guardar la nueva imagen
new_image.save("fary_ampliada.jpg")

