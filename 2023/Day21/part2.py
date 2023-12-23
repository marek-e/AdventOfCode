f = open("input.txt", "r").read()

data = f.split("\n")
n = len(data)
sparse = {(i, j) for i in range(n) for j in range(n) if data[i][j] in ".S"}
S = next((i, j) for i in range(n) for j in range(n) if data[i][j] == "S")
DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def t_add(a, b):
    return ((a[0] + b[0]), (a[1] + b[1]))


def mod_p(a):
    return (a[0] % n, a[1] % n)


visited, new, cache = {S}, {S}, {0: 1}
k, r = 26501365 // n, 26501365 % n

for c in range(1, r + 2 * n + 1):
    visited, new = new, {
        np
        for p in new
        for di in DIRS
        for np in [t_add(p, di)]
        if np not in visited and mod_p(np) in sparse
    }
    cache[c] = len(new) + (cache[c - 2] if c > 1 else 0)

d2 = cache[r + 2 * n] + cache[r] - 2 * cache[r + n]
d1 = cache[r + 2 * n] - cache[r + n]
print(cache[r + 2 * n] + (k - 2) * (2 * d1 + (k - 1) * d2) // 2)
