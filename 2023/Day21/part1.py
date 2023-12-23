f = open("input.txt", "r").read()


grid = list(map(list, f.split("\n")))

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

n = len(grid)
m = len(grid[0])

q = set()
for i in range(n):
    for j in range(m):
        if grid[i][j] == "S":
            q.add((i, j))

DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for _ in range(64):
    nq = set()
    for x, y in q:
        for dx, dy in DIRS:
            nx = x + dx
            ny = y + dy
            if grid[nx % n][ny % m] != "#":
                nq.add((nx, ny))
    q = nq

print(len(q))
