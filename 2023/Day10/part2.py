f = open("input.txt", "r").read()
grid = f.split("\n")
H = len(grid)
W = len(grid[0])

O = [[0] * W for _ in range(H)]

ax, ay = 0, 0
for i in range(H):
    for j in range(W):
        if "S" in grid[i]:
            ax = i
            ay = grid[i].find("S")

# rightward downward leftward upward
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
happy = ["-7J", "|LJ", "-FL", "|F7"]
S_dirs = []
for i in range(4):
    pos = dirs[i]
    bx = ax + pos[0]
    by = ay + pos[1]
    if bx >= 0 and bx <= H and by >= 0 and by <= W and grid[bx][by] in happy[i]:
        S_dirs.append(i)
S_valid = 3 in S_dirs

# rightward downward leftward upward
transform = {
    (0, "-"): 0,
    (0, "7"): 1,
    (0, "J"): 3,
    (2, "-"): 2,
    (2, "F"): 1,
    (2, "L"): 3,
    (1, "|"): 1,
    (1, "L"): 0,
    (1, "J"): 2,
    (3, "|"): 3,
    (3, "F"): 0,
    (3, "7"): 2,
}

curdir = S_dirs[0]
cx = ax + dirs[curdir][0]
cy = ay + dirs[curdir][1]
O[ax][ay] = 1
ln = 1
while (cx, cy) != (ax, ay):
    O[cx][cy] = 1
    ln += 1
    curdir = transform[(curdir, grid[cx][cy])]
    cx = cx + dirs[curdir][0]
    cy = cy + dirs[curdir][1]
print(ln // 2)  # part 1

ct = 0
for i in range(H):
    inn = False
    for j in range(W):
        if O[i][j]:
            if grid[i][j] in "|JL" or (grid[i][j] == "S" and S_valid):
                inn = not inn
        else:
            ct += inn
print(ct)
