from classes import *
import time

def produit_vectoriel(p1, p2, p3):
    return (p2.position[0] - p1.position[0]) * (p3.position[1] - p1.position[1]) - (p2.position[1] - p1.position[1]) * (p3.position[0] - p1.position[0]) > 0

def convex_hull(points):
    if len(points) <= 1:
        return points

    # Tri des points par ordre croissant de x, puis y
    points = sorted(points, key=lambda p: (p.position[0], p.position[1]))

    # Construction de la partie inférieure
    lower = []
    for p in points:
        while len(lower) >= 2 and not produit_vectoriel(lower[-2], lower[-1], p):
            lower.pop()
        lower.append(p)

    # Construction de la partie supérieure
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and not produit_vectoriel(upper[-2], upper[-1], p):
            upper.pop()
        upper.append(p)


    hull = lower[:-1] + upper[:-1]

    # Points non dans l'enveloppe
    points_restants = [p for p in points if p not in hull]

    return hull, points_restants

def EnveloppeConvex(nuage: PointCloud):
    points = list(nuage.List_points.keys())
    points_restants = points

    while len(points_restants) > 1:
        hull, points_restants = convex_hull(points_restants)

        SimpleGraphics.setColor(random.choice(["red", "green", "blue", "yellow", "cyan", "magenta", "orange", "purple", "brown", "gray", "black"]))
        
        for i in range(len(hull)):
            p1 = hull[i]
            p2 = hull[(i + 1) % len(hull)]
            SimpleGraphics.line(p1.position[0], p1.position[1], p2.position[0], p2.position[1])
