# Projet pour Math en Jeans 2026
# 2 Objectif
#
# n°1 : Lire coordonnées prédifinie dans un tableau excele et l'afficher dans une fenêtre graphique 
# puis placer le centre à l'aide des méthodes
# n°2 : Placement aléatoire de points selon les paramètres donnéss
#
#
# utilisation de libary : 
# simplegraphics-python et openpyxl
#
import time

from moyenneDesPoints import *
import openpyxl

import classes
from classes import *


# initialisation #
screen_width= 1200
screen_height = 900
tableau_excel = "Coordonnées_points.xlsx"


wb = openpyxl.Workbook()
File = openpyxl.load_workbook(tableau_excel)
Sheet = File.active


SimpleGraphics.resize(screen_width, screen_height)
nuage = classes.PointCloud()

def Input():

    print("--------------------------------\n Séléctionner d'abord un paramètre Basique avant d'utiliser une méthode\n \n 1 - Basique : Afficher des points aléatoirement \n 2 - Basique : afficher les points du tableau \n \n 3 - Méthode : afficher la moyenne de ces points \n \n 10 - Système : Nettoyer les points \n 11 - Système : Quitter\n -------------------------------")
    while True:
            reponse = str(input("Séléctionner un paramètre : "))

            if reponse == "1":
                nombre_de_points = int(input("Combien de points voulez-vous afficher ?"))
                nuage.createRandomPoints(nombre_de_points,screen_width,screen_height)
                setup()

            elif reponse == "2":
                  nuage.GetPoints(Sheet)
                  setup()
                    
            elif reponse == "3":
                  Moyenne(nuage)
                  setup()

            elif reponse == "10":
                  SimpleGraphics.clear()
                 
            elif reponse == "11":
                  print("Fermeture du programme...")
                  SimpleGraphics.close()
                  exit()
                  
def setup():       
        nuage.drawAllPoints()
        nuage.getPositions()
        nuage.OptimizeCloud()   


if __name__ == "__main__":
        random.seed()
        Input()