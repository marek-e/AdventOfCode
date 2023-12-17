from heapq import heappush, heappop

f = open("input.txt", "r")
board = {
    (i, j): int(col) for i, row in enumerate(f) for j, col in enumerate(row.strip())
}
DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # down, right, up, left
end = max(board)

queue = [(0, 0, 0, -1)]  # heat, x, y, disallowedDirection
seen = set()
while queue:
    heat, x, y, dd = heappop(queue)
    if (x, y) == end:
        print(heat)
        break
    if (x, y, dd) in seen:
        continue
    seen.add((x, y, dd))
    for i, (dx, dy) in enumerate(DIRS):
        if i == dd or (i + 2) % 4 == dd:
            continue
        a, b, h = x, y, heat
        for _ in range(1, 4):
            a, b = a + dx, b + dy
            if (a, b) in board:
                h += board[a, b]
                heappush(queue, (h, a, b, i))
