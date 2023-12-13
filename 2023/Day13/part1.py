import numpy as np

f = open("input.txt", "r")

board = f.read().strip().split("\n\n")
patterns = [row.split("\n") for row in board]


total = 0
for pattern in patterns:
    pattern = np.array([list(row) for row in pattern])
    rows, cols = pattern.shape
    for row in range(rows):
        shortest = min(
            row, rows - row
        )  # so we don't compare matrix segments out of bounds
        if np.all(
            pattern[row : row + shortest, :]
            == np.flipud(pattern[row - shortest : row, :])
        ):
            total += row * 100
    for col in range(cols):
        shortest = min(col, cols - col)
        if np.all(
            pattern[:, col : col + shortest]
            == np.fliplr(pattern[:, col - shortest : col])
        ):
            total += col

print(total)
