import random
import math
num_points = 1000
points = [(random.randint(0, 1000), random.randint(0, 1000)) for _ in range(num_points)]
points_with_product = [(x, y, x*y) for x, y in points]
points_sorted = sorted(points_with_product, key=lambda p: p[2])
n = len(points_sorted)
k = max(1, int(n * 0.10))
top_candidates = points_sorted[-k:]
points_coords = list(set((x, y) for x, y, *rest in top_candidates))
max_dist = -1
point_pair = None
for a in range(len(points_coords)):
    for b in range(a + 1, len(points_coords)):
        d = math.sqrt((points_coords[b][0] - points_coords[a][0])**2 + 
                      (points_coords[b][1] - points_coords[a][1])**2)
        if d > max_dist:
            max_dist = d 
            point_pair = (points_coords[a], points_coords[b])
if point_pair:
    (x1, y1), (x2, y2) = point_pair
    dx, dy = x2 - x1, y2 - y1
    dist_sq = dx**2 + dy**2
    projections = []
    for px, py in points_coords:
        if dist_sq == 0: continue
        t = ((px - x1) * dx + (py - y1) * dy) / dist_sq
        t_clamped = max(0, min(1, t))
        proj_x = x1 + t_clamped * dx 
        proj_y = y1 + t_clamped * dy
        projections.append((proj_x, proj_y))
        if projections:
         n_p = len(projections)
         center = (
         sum(p[0] for p in projections) / n_p,
         sum(p[1] for p in projections) / n_p
         )
print(f"Centre calculé : {center}")
