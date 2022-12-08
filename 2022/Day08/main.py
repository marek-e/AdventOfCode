#!/usr/bin/env python3
import numpy as np
f = open('input.txt', 'r')

grid = []
for line in f:
    grid.append([int(n)
                for n in list(line.rstrip())])
grid = np.array(grid)


def isVisible(i, j, grid):
    visT = sum([1 for t in grid[:j, i] if t >= grid[j][i]]) == 0
    visB = sum([1 for t in grid[j+1:, i] if t >= grid[j][i]]) == 0
    visL = sum([1 for t in grid[j, :i] if t >= grid[j][i]]) == 0
    visR = sum([1 for t in grid[j, i+1:] if t >= grid[j][i]]) == 0
    return visT or visB or visL or visR


def countVisible(grid):
    visible = np.zeros(grid.shape, int)
    for i in range(grid.shape[1]):
        for j in range(grid.shape[0]):
            visible[j][i] = isVisible(i, j, grid)
    return sum(sum(visible))


sol1 = countVisible(grid)
print(sol1)


def getViewDistance(h, los):
    vd = 0
    for t in los:
        vd += 1
        if t >= h:
            break
    return vd


def scenicScore(i, j, grid):
    vdTop = getViewDistance(grid[j][i], grid[:j, i][::-1])
    vdBot = getViewDistance(grid[j][i], grid[j+1:, i])
    vdLeft = getViewDistance(grid[j][i], grid[j, :i][::-1])
    vdRight = getViewDistance(grid[j][i], grid[j, i+1:])
    return vdTop*vdBot*vdLeft*vdRight


def highestScenicScore(grid):
    score = np.zeros(grid.shape, int)
    for i in range(grid.shape[1]):
        for j in range(grid.shape[0]):
            score[j][i] = scenicScore(i, j, grid)
    return np.amax(score)


sol2 = highestScenicScore(grid)
print(sol2)
