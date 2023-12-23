f = open("input.txt", "r").read().strip()

import sys

sys.setrecursionlimit(1000000)


grid = [list(r) for r in f.split("\n")]
n, m = len(grid), len(grid[0])

DIR = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}


def adj(cur):
    x, y = cur
    dirs = DIR.values()
    if grid[x][y] in "^>v<":
        dirs = [DIR[grid[x][y]]]
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if nx in range(n) and ny in range(m) and grid[nx][ny] != "#":
            yield (nx, ny)


best = 0


def dfs(cur, path, path_set):
    global best
    if cur == (n - 1, m - 2):
        best = max(best, len(path))
    for a in adj(cur):
        if a not in path_set:
            path.append(a)
            path_set.add(a)
            dfs(a, path, path_set)
            path_set.remove(a)
            path.pop(-1)


dfs((0, 1), [], set())
print(best)
