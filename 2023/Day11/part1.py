import numpy as np
from itertools import combinations

f = open("input.txt", "r")
empty_col = set()
empty_row = set()

grid = np.array([list(line.strip()) for line in f.readlines()])

for i in range(grid.shape[0]):
    if np.all(grid[i] == "."):
        empty_row.add(i)

for i in range(grid.shape[1]):
    if np.all(grid[:, i] == "."):
        empty_col.add(i)

stars = list(zip(*np.where(grid == "#")))

total = 0
for pair in list(combinations(stars, 2)):
    (a_x, a_y), (b_x, b_y) = pair
    d_x = max(a_x, b_x) - min(a_x, b_x)
    d_y = max(a_y, b_y) - min(a_y, b_y)
    count = d_x + d_y
    count += len(empty_row.intersection(range(min(a_x, b_x), max(a_x, b_x) + 1)))
    count += len(empty_col.intersection(range(min(a_y, b_y), max(a_y, b_y) + 1)))
    total += count
print(total)
