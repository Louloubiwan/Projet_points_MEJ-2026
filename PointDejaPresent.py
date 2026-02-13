import numpy as np
from scipy.spatial.distance import squareform, pdist

def PointDejaPresent(PointCloud):
    ids = list(PointCloud.List_points.keys())
    coords = np.array(list(PointCloud.List_points.values()),dtype= "float")
    D = squareform(pdist(coords , metric="euclidean"))
    avg = D.mean(axis=1)
    best_idx = np.argmin(avg)
    best_id = ids[best_idx]
    best_point = coords[best_idx]
    x,y = best_point
    print(x ," ",y)
    PointCloud.drawSinglePoint(x, y, "blue")
    