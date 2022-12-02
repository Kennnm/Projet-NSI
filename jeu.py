#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 09:00:53 2022

@author: kenji.moua
"""
import sqlite3 as sql
connexion = sql.connect('Table2')
base = connexion.cursor()



def maison():
    pass

def rond_point():
    print("1 - fouillez dans le sac\n2 - se déplacer\n3 - parler à quelqu'un\n4 - observer les alentours")
    a = input("")
    if a == "1":
        sac()
    elif a == "2":
        marche()
    elif a == "3":
        parle()
    elif a == "4":
        cherche()
    else: rond_point()

def rencontre():
    print("un blob vous fait coucou\nil semble vous dire:\nyo Alvin, ça fait longtemps ! Bon, mec, on a besoin de toi en fait.\nJ'aurai besoin que tu me prête ton livre dont on avait parlé il y a une smeaine, se serait bien.")
    print("Première mission : retrouver le livre que le blob vous demande:\nallez dans votre maison, en face de vous.")
    print("déplacez vous:\nutilisez la touche Z")
    a = input("")
   # if a in "Zz":
       # position +=1
    print("vous voyez un sac à l'entrée de la maison ")
    maison()
    
def histoire():
    print("Tu te réveilles allongé par terre.")
    print("en face de vos est un chemin")
    print("avancer ? o/n")
    b = input("\n")
    if b == "n":
        print("vous restez là comme un con")
    elif b =="o":
        print("vous entrez dans un village")
        rencontre()
    else: histoire()
    



#histoire()




def sac():
	print("Si vous souhaitez ouvrir le journal appuyez sur la touche 'j' ")
	print("Si vous souhaitez consulter vos objets appuyez sur la touche 'o' ")
	
	a = input("\n")
	if a == "j":
		journal()
	elif a == "o":
		objets()


def mouvement():
	
	position = 0

	d = input("Si vous voulez vous déplacez appuyez sur la touche 'm': ")
	
	if d == "m" and position%2 == 0:
			
		print(" 'z' = Vous vous dans le jardin devant le maison")
		print(" 'd' = Vous allez devant la forêt")
		print(" 's' = Vous pouvez vous dirigez sur le sentier menant à la montagne")
		print(" 'q' = Vous pouvez vous dirigez à l'entrée du village")

		s = input()
	
		if s == "z":
			print("Vous êtes dans le jardin")
			
			print("Vous pouvez aller dans le salon")
			
		if s == "d":
			print("Vous vous trouvez devant la forêt")
			position +=2
		if s == "s":
			print("Vous êtes juste devant le sentier qui vous mènera à la montagne")
			position += 4
		if s == "q":
			print("Vous êtes à l'entrée du village")
			position += 6
			
	if d == "m" and position%2 == 1:
		
		if position == 1:
			print("")


























