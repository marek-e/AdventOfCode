import numpy as np

f = open("input.txt", "r")

board = f.read().strip().split("\n\n")
patterns = [row.split("\n") for row in board]


total = 0
for pattern in patterns:
    pattern = np.array([list(row) for row in pattern])
    rows, cols = pattern.shape
    for row in range(rows):
        shortest = min(row, rows - row)
        matches = np.count_nonzero(
            pattern[row : row + shortest, :]
            == np.flipud(pattern[row - shortest : row, :])
        )
        if matches == shortest * cols - 1:
            total += row * 100
    for col in range(cols):
        shortest = min(col, cols - col)
        matches = np.count_nonzero(
            pattern[:, col : col + shortest]
            == np.fliplr(pattern[:, col - shortest : col])
        )
        if matches == rows * shortest - 1:
            total += col

print(total)
