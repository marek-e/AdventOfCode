f = open("input.txt", "r").read().strip()

import sys
from collections import defaultdict

sys.setrecursionlimit(1000000)


grid = [list(r) for r in f.split("\n")]
n, m = len(grid), len(grid[0])

DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def adj(cur):
    x, y = cur
    for dx, dy in DIRS:
        nx, ny = x + dx, y + dy
        if nx in range(n) and ny in range(m) and grid[nx][ny] != "#":
            yield (nx, ny)


v = set()
dd = defaultdict(list)

for i in range(n):
    for j in range(m):
        if grid[i][j] != "#":
            if len(list(adj((i, j)))) > 2:
                v.add((i, j))
v.add((0, 1))
v.add((n - 1, m - 2))


for x, y in v:
    q = []
    q.append((x, y))
    seen = {(x, y)}
    dist = 0
    while len(q) > 0:
        nq = []
        dist += 1
        for c in q:
            for a in adj(c):
                if a not in seen:
                    if a in v:
                        dd[x, y].append((dist, a))
                        seen.add(a)
                    else:
                        seen.add(a)
                        nq.append(a)
        q = nq


best = 0


def dfs(cur, path_set, total_dist):
    global best
    if cur == (n - 1, m - 2):
        best = max(best, total_dist)
    for da, a in dd[cur]:
        if a not in path_set:
            path_set.add(a)
            dfs(a, path_set, total_dist + da)
            path_set.remove(a)


dfs((0, 1), set(), 0)
print(best)
