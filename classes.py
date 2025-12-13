import openpyxl
import SimpleGraphics



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
    def drawAllPoints(self, color): # elle sert a rien mais on va quand meme la garder au cas ou
        for p in self.List_points:
            print("color = " , p.color)
            SimpleGraphics.setFill(p.color)
            SimpleGraphics.circle(p.x,p.y ,10)
    def drawSinglePoint(self,x,y,color):
        SimpleGraphics.setFill(color)
        SimpleGraphics.circle(x,y, 10)