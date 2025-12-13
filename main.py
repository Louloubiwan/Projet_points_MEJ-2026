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
from time import sleep

import openpyxl

import classes
from classes import *
# initialisation #

tableau_excel = "Coordonnées_points.xlsx"


wb = openpyxl.Workbook()
File = openpyxl.load_workbook(tableau_excel)
Sheet = File.active



def setup():
    SimpleGraphics.resize(1200, 900)
    nuage = classes.PointCloud()
    nuage.GetPoints(Sheet)
    nuage.addPoint(400,450, "green")
    nuage.addPoint(400,300, "purple")
    nuage.addPoint(400,550, "black")

    for i in nuage.List_points:
        print(i.color)

if __name__ == "__main__":
        setup()