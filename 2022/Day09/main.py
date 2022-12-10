#!/usr/bin/env python3
f = open('input.txt', 'r')


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '('+str(self.x)+','+str(self.y)+')'

    def is_far(self, P):
        return abs(self.x - P.x) > 1 or abs(self.y - P.y) > 1

    def up(self):
        self.y += 1

    def down(self):
        self.y -= 1

    def left(self):
        self.x -= 1

    def right(self):
        self.x += 1

    def get_pos(self):
        return (self.x, self.y)


H = Point(0, 0)
T = Point(0, 0)
visited = set()


def followHead():
    if T.x != H.x and T.y != H.y:
        if H.x > T.x and H.y > T.y:
            T.x += 1
            T.y += 1
        if H.x > T.x and H.y < T.y:
            T.x += 1
            T.y -= 1
        if H.x < T.x and H.y > T.y:
            T.x -= 1
            T.y += 1
        if H.x < T.x and H.y < T.y:
            T.x -= 1
            T.y -= 1
    elif T.x == H.x:
        if H.y > T.y:
            T.up()
        else:
            T.down()
    elif T.y == H.y:
        if H.x > T.x:
            T.right()
        else:
            T.left()


def move(direction):
    if direction == 'U':  # UP
        H.up()
    if direction == 'D':  # DOWN
        H.down()
    if direction == 'R':  # RIGHT
        H.right()
    if direction == 'L':  # LEFT
        H.left()
    if T.is_far(H):
        followHead()
    visited.add(T.get_pos())


for line in f:
    action = line.strip().split(' ')
    direction = action[0]
    rep = int(action[1])

    for i in range(rep):
        move(direction)
        # print('H :', H, '     T :', T)

print(len(visited))
