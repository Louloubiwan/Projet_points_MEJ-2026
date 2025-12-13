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

import openpyxl
import SimpleGraphics
from SimpleGraphics import circle

# initialisation #

tableau_excel = "Coordonnées_points.xlsx"


wb = openpyxl.Workbook()
File = openpyxl.load_workbook(tableau_excel)
Sheet = File.active



List_points = []


class Point:
    def __init__(self, x, y):
        self.x = x # Position en x
        self.y = y # Position en y


class PointCloud:
    def __init__(self):
        pass
    def GetPoints(self):
        for row in Sheet.iter_rows(min_row=2, values_only=True):
            List_points.append(Point(row[1],row[2]))
    def draw(self):
        for p in List_points:
            circle(p.x,p.y ,100 )
            text
SimpleGraphics.resize(1200, 900)


nuage = PointCloud
nuage.GetPoints(nuage)
for i in List_points:
    print(i.x,i.y)
nuage.draw(nuage)