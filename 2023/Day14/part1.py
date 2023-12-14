f = open("input.txt", "r").readlines()
board = [list(line.strip()) for line in f]


def calculate_load(lines):
    return sum(r * row.count("O") for r, row in enumerate(lines[::-1], 1))


def tilt_north(i, j, grid):
    while i > 0 and grid[i - 1][j] == ".":
        grid[i][j] = "."
        grid[i - 1][j] = "O"
        i -= 1
    return (i, j)


rocks = [
    (i, j)
    for j in range(len(board[0]))
    for i in range(len(board))
    if board[i][j] == "O"
]
for i, j in rocks:
    tilt_north(i, j, board)

print(calculate_load(board))
