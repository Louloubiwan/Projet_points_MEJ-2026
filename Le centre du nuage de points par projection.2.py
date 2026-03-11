import random
import math
points_coords = [(random.random(), random.random()) for _ in range(1000)]
x1, y1 = random.random(), random.random()
x2, y2 = random.random(), random.random()
xm = (x1 + x2) / 2
ym = (y1 + y2) / 2
AB = math.sqrt((x2-x1)**2 + (y2-y1)**2)
r = AB / 2
x1, y1 = points_coords[0]
x2, y2 = points_coords[1]
center_x = (x1 + x2) / 2
center_y = (y1 + y2) / 2
radius_segment = math.sqrt((x2 - x1)**2 + (y2 - y1)**2) / 2
max_radius = radius_segment
for p in points_coords:
    d = math.sqrt((p[0] - center_x)**2 + (p[1] - center_y)**2)
    if d > max_radius:
        max_radius = d
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
