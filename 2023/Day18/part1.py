f = open("input.txt", "r")

plan = [l.split() for l in f.readlines()]

dirs = {"R": (0, 1), "L": (0, -1), "U": (-1, 0), "D": (1, 0)}

x, y, p = 0, 0, 0
area = 0
for _dir, dist, _ in plan:
    dx, dy = dirs[_dir]
    dist = int(dist)
    x, y, p = x + dx * dist, y + dy * dist, p + dist
    area += (x + dx * dist) * dy * dist

print(abs(area) + p // 2 + 1)
