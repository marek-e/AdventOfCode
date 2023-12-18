f = open("input.txt", "r")

plan = [l.split() for l in f.readlines()]

dirs = {"0": (0, 1), "1": (1, 0), "2": (0, -1), "3": (-1, 0)}

x, y, p = 0, 0, 0
area = 0
for _, _, code in plan:
    _dir, dist = code[7], int(code[2:7], 16)
    dx, dy = dirs[_dir]
    x, y, p = x + dx * dist, y + dy * dist, p + dist
    area += (x + dx * dist) * dy * dist

print(abs(area) + p // 2 + 1)
