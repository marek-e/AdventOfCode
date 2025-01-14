from itertools import count

f = open("input.txt", "r").readlines()
board = [list(line.strip()) for line in f]


def tilt_north(i, j, grid):
    while i > 0 and grid[i - 1][j] == ".":
        grid[i][j], grid[i - 1][j] = ".", "O"
        i -= 1
    return (i, j)


def tilt_west(i, j, grid):
    while j > 0 and grid[i][j - 1] == ".":
        grid[i][j], grid[i][j - 1] = ".", "O"
        j -= 1
    return (i, j)


def tilt_south(i, j, grid):
    while i < len(grid) - 1 and grid[i + 1][j] == ".":
        grid[i][j], grid[i + 1][j] = ".", "O"
        i += 1
    return (i, j)


def tilt_east(i, j, grid):
    while j < len(grid[0]) - 1 and grid[i][j + 1] == ".":
        grid[i][j], grid[i][j + 1] = ".", "O"
        j += 1
    return (i, j)


def calc_load(g):
    return sum(i * row.count("O") for i, row in enumerate(g[::-1], start=1))


def cycle(rocks, grid):
    keys = [
        lambda x: x[1],
        lambda x: -x[0],
        lambda x: -x[1],
        lambda x: x[0],
    ]
    for k, f in enumerate((tilt_north, tilt_west, tilt_south, tilt_east)):
        n_rocks = []
        for i, j in rocks:
            ni, nj = f(i, j, grid)
            n_rocks.append((ni, nj))
        rocks = sorted(n_rocks, key=keys[k % 4])
    return (rocks, grid)


def find_cycle(rocks, grid):
    seen = {"\n".join("".join(row) for row in grid): 0}
    for i in count(start=1):
        rocks, grid = cycle(rocks, grid)
        cur = "\n".join("".join(row) for row in grid)
        if cur in seen:
            return (seen[cur], i - seen[cur], seen)
        seen[cur] = i


rocks = [
    (i, j)
    for j in range(len(board[0]))
    for i in range(len(board))
    if board[i][j] == "O"
]
start, length, seen = find_cycle(rocks, board)
r_seen = {v: k for k, v in seen.items()}
res = r_seen[(start + (1000000000 - start) % length)]
print(calc_load(res.split("\n")))
