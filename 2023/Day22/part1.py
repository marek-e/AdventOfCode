f = open("input.txt", "r").read()

from collections import defaultdict

bricks = []
for line in f.split("\n"):
    a, b = line.split("~")
    a = list(map(int, a.split(",")))
    b = list(map(int, b.split(",")))
    bricks.append((a, b))

n = len(bricks)

bricks.sort(key=lambda x: x[0][2])

highest = defaultdict(lambda: (0, -1))
bad = set()
graph = [[] for _ in range(n)]
for idx, b in enumerate(bricks):
    max_h = -1
    support_set = set()
    for x in range(b[0][0], b[1][0] + 1):
        for y in range(b[0][1], b[1][1] + 1):
            if highest[x, y][0] + 1 > max_h:
                max_h = highest[x, y][0] + 1
                support_set = {highest[x, y][1]}
            elif highest[x, y][0] + 1 == max_h:
                support_set.add(highest[x, y][1])

    for x in support_set:
        if x != -1:
            graph[x].append(idx)

    if len(support_set) == 1:
        bad.add(support_set.pop())

    fall = b[0][2] - max_h
    if fall > 0:
        b[0][2] -= fall
        b[1][2] -= fall

    for x in range(b[0][0], b[1][0] + 1):
        for y in range(b[0][1], b[1][1] + 1):
            highest[x, y] = (b[1][2], idx)

print(len(bricks) - len(bad) + 1)
