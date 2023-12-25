from collections import deque

f = open("input.txt", "r")

lines = f.read().splitlines()

board = {
    (row_n, col_n): col
    for row_n, row in enumerate(lines)
    for col_n, col in enumerate(row)
}

dirs = {
    "|": [(1, 0), (-1, 0)],
    "-": [(0, 1), (0, -1)],
    "7": [(1, 0), (0, -1)],
    "L": [(-1, 0), (0, 1)],
    "J": [(-1, 0), (0, -1)],
    "F": [(1, 0), (0, 1)],
    "S": [(0, 1), (0, -1)],  # set manually from input
}

S = next(z for z, x in board.items() if x == "S")
seen = {S}
q = deque([(S, 0)])

while q:
    z, dist = q.popleft()
    for dz in dirs[board[z]]:
        new_z = (z[0] + dz[0], z[1] + dz[1])
        if new_z not in seen:
            q.append((new_z, dist + 1))
            seen.add(new_z)

print(dist)
