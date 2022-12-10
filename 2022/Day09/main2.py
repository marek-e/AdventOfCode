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

    def follow(self, P):
        if self.x != P.x and self.y != P.y:
            if P.x > self.x and P.y > self.y:
                self.x += 1
                self.y += 1
            if P.x > self.x and P.y < self.y:
                self.x += 1
                self.y -= 1
            if P.x < self.x and P.y > self.y:
                self.x -= 1
                self.y += 1
            if P.x < self.x and P.y < self.y:
                self.x -= 1
                self.y -= 1
        elif self.x == P.x:
            if P.y > self.y:
                self.up()
            else:
                self.down()
        elif self.y == P.y:
            if P.x > self.x:
                self.right()
            else:
                self.left()


def display_rope():
    s = '['
    for node in rope:
        s += str(node)
    s += ']'
    print(s)


rope = []
for i in range(10):
    rope.append(Point(0, 0))
visited = set()


def move(direction):
    H = rope[0]
    if direction == 'U':  # UP
        H.up()
    if direction == 'D':  # DOWN
        H.down()
    if direction == 'R':  # RIGHT
        H.right()
    if direction == 'L':  # LEFT
        H.left()
    for i in range(1, len(rope)):
        if rope[i].is_far(rope[i-1]):
            rope[i].follow(rope[i-1])

    visited.add(rope[-1].get_pos())


for line in f:
    action = line.strip().split(' ')
    direction = action[0]
    rep = int(action[1])

    for i in range(rep):
        move(direction)
        # display_rope()

print(len(visited))
