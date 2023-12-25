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
graph = [[] for _ in range(n)]
for idx, brick in enumerate(bricks):
    max_h = -1
    support_set = set()
    for x in range(brick[0][0], brick[1][0] + 1):
        for y in range(brick[0][1], brick[1][1] + 1):
            if highest[x, y][0] + 1 > max_h:
                max_h = highest[x, y][0] + 1
                support_set = {highest[x, y][1]}
            elif highest[x, y][0] + 1 == max_h:
                support_set.add(highest[x, y][1])

    for x in support_set:
        if x != -1:
            graph[x].append(idx)

    fall = brick[0][2] - max_h
    if fall > 0:
        brick[0][2] -= fall
        brick[1][2] -= fall

    for x in range(brick[0][0], brick[1][0] + 1):
        for y in range(brick[0][1], brick[1][1] + 1):
            highest[x, y] = (brick[1][2], idx)


def count(idx, graph):
    l = [0 for _ in range(n)]
    for j in range(n):
        for i in graph[j]:
            l[i] += 1
    q = [idx]
    count = -1
    while len(q) > 0:
        count += 1
        x = q.pop()
        for i in graph[x]:
            l[i] -= 1
            if l[i] == 0:
                q.append(i)

    return count


print(sum(count(x, graph) for x in range(n)))
