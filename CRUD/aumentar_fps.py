from PIL import Image, ImageEnhance, ImageFilter
import numpy as np

# Cargar las imágenes de fondo y el dragón
fondo_path = "/mnt/data/fondo.jpg"
dragon_path = "/mnt/data/m_img_04_s.png"

fondo_img = Image.open(fondo_path).convert("RGBA")
dragon_img = Image.open(dragon_path).convert("RGBA")

# Redimensionar el dragón para que sea más grande
dragon_scale_factor = 2  # Escalar el dragón para que sea más grande
dragon_resized = dragon_img.resize((int(dragon_img.width * dragon_scale_factor), int(dragon_img.height * dragon_scale_factor)))

# Colocar el dragón en la posición baja del fondo
fondo_width, fondo_height = fondo_img.size
dragon_width, dragon_height = dragon_resized.size
position_x = (fondo_width - dragon_width) // 2  # Centrando horizontalmente
position_y = fondo_height - dragon_height  # Colocándolo en el suelo

# Superponer el dragón en el fondo
fondo_with_dragon = fondo_img.copy()
fondo_with_dragon.paste(dragon_resized, (position_x, position_y), dragon_resized)

# Añadir partículas de rayos
# Crear un filtro de rayos en una capa de ruido
rayo_layer = Image.new("RGBA", fondo_with_dragon.size, (0, 0, 0, 0))
for _ in range(150):  # Generar 150 partículas de rayos
    x = np.random.randint(0, fondo_width)
    y = np.random.randint(position_y, fondo_height)  # Partículas solo en la parte inferior
    size = np.random.randint(5, 10)
    opacity = np.random.randint(50, 150)
    particle = Image.new("RGBA", (size, size), (255, 255, 255, opacity))
    rayo_layer.paste(particle, (x, y), particle)

# Combinar la capa de rayos con el fondo
final_image = Image.alpha_composite(fondo_with_dragon, rayo_layer)

# Guardar la imagen final
output_path = "/mnt/data/combined_image_with_rays.png"
final_image.save(output_path)

output_path
