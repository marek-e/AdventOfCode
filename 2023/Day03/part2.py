engine_schematic = open("input.txt", "r")

board = list(engine_schematic.read().splitlines())

symbols = {
    (r, c)
    for r in range(len(board))
    for c in range(len(board[0]))
    if board[r][c] not in "0123456789."
}


def has_symbol(x, y):
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if (x + dx, y + dy) in symbols:
                return True
    return False


gears = []

for i, row in enumerate(board):
    current = ""
    isAdjacent = False
    for j in range(len(row)):
        if row[j].isdigit():
            current += row[j]
            if not isAdjacent and has_symbol(i, j):
                isAdjacent = True
            if j == len(row) - 1 and isAdjacent:  # last digit in row
                gears.append((i, j - len(current) + 1, len(current)))
        elif isAdjacent:
            gears.append((i, j - len(current), len(current)))
            isAdjacent = False
            current = ""
        else:
            isAdjacent = False
            current = ""

stars = [
    [row, col]
    for row in range(len(board))
    for col in range(len(board[0]))
    if board[row][col] == "*"
]

gearRatios = 0
for rowStar, colStar in stars:
    neighbors = [
        [r, c, l]
        for r, c, l in gears
        if r - 1 <= rowStar <= r + 1 and c - 1 <= colStar <= c + l
    ]
    if len(neighbors) == 2:
        values = [
            int("".join(board[row][col : col + length]))
            for row, col, length in neighbors
        ]
        gearRatios += values[0] * values[1]

print(gearRatios)
