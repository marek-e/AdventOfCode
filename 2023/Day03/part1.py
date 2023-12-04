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


total = 0

for i, row in enumerate(board):
    current = ""
    isAdjacent = False
    for j in range(len(row)):
        if row[j].isdigit():
            current += row[j]
            if not isAdjacent and has_symbol(i, j):
                isAdjacent = True
            if j == len(row) - 1 and isAdjacent:  # last digit in row
                total += int(current)
        elif isAdjacent:
            total += int(current)
            isAdjacent = False
            current = ""
        else:
            isAdjacent = False
            current = ""

print(total)
