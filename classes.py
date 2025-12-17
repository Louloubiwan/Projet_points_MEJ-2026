import random
from operator import truediv

import SimpleGraphics
from SimpleGraphics import setAutoUpdate


class Point:
    def __init__(self, x, y, color):
        self.x = x # Position en x
        self.y = y # Position en y
        self.color = color # couleur du point

class PointCloud:
    def __init__(self,):
        self.List_points = []

    def GetPoints(self,sheet):
        for row in sheet.iter_rows(min_row=2, values_only=True):
            self.addPoint(row[1],row[2], "red")

    def addPoint(self, x,y, color):
        self.List_points.append(Point(x, y, color))
        self.drawSinglePoint(x,y, color)

    def drawAllPoints(self): # elle sert a rien mais on va quand meme la garder au cas ou
        for p in self.List_points:
            print("color = " , p.color)
            self.drawSinglePoint(p.x ,p.y, "red")
    @staticmethod
    def drawSinglePoint(x, y, color):
        SimpleGraphics.setFill(color)
        SimpleGraphics.circle(x,y, 10)

    def createRandomPoints(self,number_of_points, bound_x , bound_y):
        setAutoUpdate(False)
        for i in range(number_of_points):
            self.addPoint(random.randrange(0, bound_x), random.randrange(0, bound_y) , "red")
        setAutoUpdate(True)
