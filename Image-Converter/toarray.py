import os
import matplotlib.pyplot as plt
import numpy as np

def process_image_to_bitmap(filepath):
    # Cargar la imagen
    img = plt.imread(filepath)
    
    # Convertir a escala de grises si tiene canal alfa o es RGB
    if img.shape[-1] == 4:
        img = img[..., :3]  # Ignorar canal alfa si existe
    gray_img = np.dot(img[..., :3], [0.299, 0.587, 0.114])
    
    # Convertir a bitmap binario (0 y 1)
    bitmap_array = (gray_img > 0.005).astype(int)
    
    # Formatear el array para el formato de sprite
    sprite_lines = ["[" + ", ".join(map(str, row)) + "]" for row in bitmap_array]
    sprite_text = "[\n" + ",\n".join(sprite_lines) + "\n]"
    
    return sprite_text

def process_folder_to_sprites(folder_path, output_file="sprites_output.txt"):
    with open(output_file, "w") as file:
        for filename in os.listdir(folder_path):
            if filename.endswith((".png", ".jpg", ".jpeg")):
                filepath = os.path.join(folder_path, filename)
                sprite_text = process_image_to_bitmap(filepath)
                
                # Escribir cada sprite con su nombre de archivo
                file.write(f"{filename} = {sprite_text}\n\n")
    print(f"Sprites guardados en {output_file}")

# Ruta de la carpeta con las imágenes
folder_path = "."  # Cambia a la ruta de tu carpeta
process_folder_to_sprites(folder_path)