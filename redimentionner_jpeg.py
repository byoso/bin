#! /usr/bin/env python3
# -*- coding : utf-8 -*-

from PIL import Image
import os
import sys

params = len(sys.argv)
quality = 10
ratio = 1.0
repertoire = os.getcwd()
nom_sous_repertoire = "images_redim"
compteur = 0

notice = """
Synopsis de l'utilisation :

redimentioner_images.py [ratio, default=1.0] [quality, default=10 (max=100)]
exemple : redimentioner_images.py 1 90
            """
redim = True

def redimention(params, quality, ratio, repertoire, nom_sous_repertoire, compteur):
    nom_sous_repertoire = f"images_redim_R_{ratio}_Q_{quality}"
    if not os.path.exists(os.path.join(repertoire, nom_sous_repertoire)):
        os.makedirs(os.path.join(repertoire, nom_sous_repertoire))

    for item in os.listdir(repertoire):
        if os.path.isfile(item):
            f, e = os.path.splitext(item)
            if e in ['.jpg', '.jpeg', '.JPG', '.JPEG']:
                im = Image.open(item)
                size = im.size
                new_image_size = tuple([int(x * ratio) for x in size])
                imResize = im.resize(new_image_size, Image.ANTIALIAS)
                imResize.save(os.path.join(os.path.join(
                    repertoire, nom_sous_repertoire), f) + e, 'JPEG', quality=quality)
                compteur += 1
                print(str(compteur) + " " + str(im.size) + " => " +
                      str(new_image_size) + " | Ratio : " + str(ratio) + " | Quality : " + str(quality))


if params > 1:
    if sys.argv[1] in ['-h', 'h', '--help', 'help']:
        print(notice)
        redim = False
    else:
        ratio = float(sys.argv[1])
        redim = True
if params > 2:
    quality = int(sys.argv[2])
    redim = True

if params > 3:
    print("=== COMMANDE INVALIDE ===")
    print(notice)
    redim = False


if redim :
    print("dans : " + repertoire)
    redimention(params, quality, ratio, repertoire,
                nom_sous_repertoire, compteur)
