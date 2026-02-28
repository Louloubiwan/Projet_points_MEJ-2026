from classes import * 


def ou_aller(p1, p2, p3):
    return (p2.position[0] - p1.position[0]) * (p3.position[1] - p1.position[1]) - (p2.position[1] - p1.position[1]) * (p3.position[0] - p1.position[0]) > 0


def convex_hull(point):

   # créer la partie inférieure de l'enveloppe convexe
    lower = []
    for p in point:
        while len(lower) >= 2 and not ou_aller(lower[-2], lower[-1], p):
            lower.pop()
        lower.append(p)

    # créer la partie supérieure de l'enveloppe convexe
    upper = []
    for p in reversed(point):
        while len(upper) >= 2 and not ou_aller(upper[-2], upper[-1], p):
            upper.pop()
        upper.append(p)

    for p in point: # Les points qui ne sont pas dans l'enveloppe convexe
        if p in lower and p in upper:
            PointsRestant.remove(p) #Les points restant sont les points qui ne sont pas dans l'enveloppe convexe
    print(PointsRestant)

    # concaténer les parties inférieure et supérieure pour obtenir l'enveloppe convexe complète
    return lower[:-1] + upper[:-1]



def EnveloppeConvex(nuage: PointCloud):
    global PointsRestant

    points = list(nuage.List_points.keys()) # Tout les points du nuage
    points.sort(key=lambda p: (p.position[0], p.position[1])) # Tri des points par ordre croissant de leurs coordonnées x, puis y

    PointsRestant = points # valeur initial : le nombre de points restant est égale au nombre de points total
    PointsRestant = list(PointsRestant)
    PointsRestant.sort(key=lambda p: (p.position[0], p.position[1]))

    while len(PointsRestant) > 1:
        hull_points = convex_hull(PointsRestant)


        SimpleGraphics.setColor(random.choice(["red", "green", "blue", "yellow", "cyan", "magenta", "orange", "purple", "pink", "brown", "gray"]))
        for i in range(len(hull_points)):
            p1 = hull_points[i]
            p2 = hull_points[(i + 1) % len(hull_points)]  # Connecter le dernier point au premier pour fermer l'enveloppe convexe
            SimpleGraphics.line(p1.position[0], p1.position[1], p2.position[0], p2.position[1])

    
