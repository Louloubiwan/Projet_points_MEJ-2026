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



def setup():
    SimpleGraphics.resize(screen_width, screen_height)
    nuage = classes.PointCloud()
    nuage.createRandomPoints(100000,screen_width,screen_height )
    Moyenne(nuage)
if __name__ == "__main__":
        random.seed()
        setup()