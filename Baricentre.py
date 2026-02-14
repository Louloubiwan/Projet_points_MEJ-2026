from classes import *
def baricentre(points : PointCloud):
    CouplePoint = {}
    Baricentre = {}
    point_list = list(points.List_points.keys())
    
    for i in range(0, len(point_list) - 1, 2):
        p = point_list[i]
        p_next = point_list[i + 1]
        
        if p not in CouplePoint:
            points1X = p.position[0]
            points1Y = p.position[1]
            CouplePoint[p] = (points1X, points1Y)

            points2X = p_next.position[0]
            points2Y = p_next.position[1]

            CouplePoint[p_next] = (points2X, points2Y)

            MiddlePointX = (points1X + points2X) / 2
            MiddlePointY = (points1Y + points2Y) / 2
            Baricentre[p] = (MiddlePointX, MiddlePointY)
 

    CouplePoint.clear()

    while len(Baricentre) != 1:
        baricentre_keys = list(Baricentre.keys())
        for i in range(0, len(baricentre_keys) - 1, 2):
            point1 = baricentre_keys[i]
            point2 = baricentre_keys[i + 1]           
            if i not in Baricentre:
                points1X_baricentre = Baricentre[point1][0]
                points1Y_baricentre = Baricentre[point1][1]
                CouplePoint[point1] = (points1X_baricentre, points1Y_baricentre)
                points2X_baricentre = Baricentre[point2][0]
                points2Y_baricentre = Baricentre[point2][1]
                CouplePoint[point2] = (points2X_baricentre, points2Y_baricentre)

                MiddlePoint_baricentreX = (points1X_baricentre + points2X_baricentre) / 2
                MiddlePoint_baricentreY = (points1Y_baricentre + points2Y_baricentre) / 2
                MiddlePoint_baricentre = (MiddlePoint_baricentreX, MiddlePoint_baricentreY)

                del Baricentre[point1]
                if point2 in Baricentre:
                    del Baricentre[point2]
                Baricentre[-1] = MiddlePoint_baricentre


    final_baricentre_coords = list(Baricentre.values())[0]
    points.drawSinglePoint(final_baricentre_coords[0], final_baricentre_coords[1], "blue")
    return
            
                

    
