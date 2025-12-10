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



List_points = {} 


class Point:
    def __init__(self, x, y):
        self.x = x # Position en x
        self.y = y # Position en y

    def draw(self):     
        point = SimpleGraphics.circle(100, 100, 20)




SimpleGraphics.resize(1200, 900)

point = Point(400, 400)
point.draw()