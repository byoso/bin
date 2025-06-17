#! /usr/bin/env python3
import os
from PIL import Image
from pprint import pprint


# === Configuration ===
images_folder = os.path.abspath(os.getcwd())  # Dossier contenant les images
output_file = "animation.gif"  # Nom du GIF en sortie
duree_par_image = 200  # Durée d'affichage de chaque image (en ms)

# === Get and sort images ===
fichiers = sorted([
    f for f in os.listdir(images_folder)
    if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.webp', '.gif'))
])
if output_file in fichiers:
    fichiers.remove(output_file)
pprint(fichiers)
if not fichiers:
    print("Aucune image trouvée dans le dossier.")
    exit()

images = [Image.open(os.path.join(images_folder, f)).convert("RGBA") for f in fichiers]

# Resize imagees at the size of the first one
largeur, hauteur = images[0].size
images = [img.resize((largeur, hauteur)) for img in images]

# === Create the animated gif GIF ===
images[0].save(
    output_file,
    save_all=True,
    append_images=images[1:],
    duration=duree_par_image,
    loop=0
)

print(f"GIF successfully animated !: {images_folder}/{output_file}")
