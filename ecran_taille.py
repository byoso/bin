#! /usr/bin/python3

import math
import os

sortie = ""

def ecran(diag=27, ry=16, rx=9):
    y = math.sqrt((diag**2)/((rx/ry)**2+1))
    x = (rx/ry)*y
    return x, y

def tableau(x, y):
	x = int(x/2)
	y = int(y/2)
	schema = '\n Schematisation :\n'
	for i in range(x):
		for i in range(y):
			schema += '..'
		schema += '\n'
	
	return schema


def main(sortie=''):
	sortie += "\n ========================= \n"
	diag = float(input('diagonale : '))
	ratiox= float(input("ratio X de l'écran : "))
	ratioy = float(input("ratio Y de l'écran : "))
	sortie += f"~~ Ecran {diag}, Ratio {int(ratiox)}/{int(ratioy)} ~~\n"

	x, y = ecran(diag, ratiox, ratioy)
	surface = x*y
	conv = input('Si vous avez des pouces, convertir en cm ?(y/n)')

	if conv.lower() == 'y':
		diag = diag * 2.54
		x = 2.54 * x
		y = 2.54 * y
		surface = x*y
		resultat = f'diagonale : {diag} cm\nhauteur : {x} cm\nlargeur : {y} cm\nsurface : {surface} cm2'
		sortie += resultat
		sortie += tableau(x,y)
		return relanceur(sortie)
	else:
		resultat = f'diagonale : {diag} \nhauteur : {x}\nlargeur : {y}\nsurface : {surface} cm2'
		sortie += resultat
		sortie += tableau(x,y)
		return relanceur(sortie)


def relanceur(sortie):
	suite = input("voulez-vous comparer avec un autre ecran (C), enregistrer (R), ou finir sans enregistrer(ANY) ?")
	if suite.lower() == 'c':
		return main(sortie)
	if suite.lower() == 'r':
		sortie += '\n'
		folder = (os.getcwd())
		fich = folder+'/tailles_ecrans.txt'
		with open(fich, 'w') as fichier:
			fichier.write(sortie)
		print(f'fichier {fich} enregistré')
		return print(sortie)
	else:
		sortie += '\n'
		return print(sortie)
		
main()
