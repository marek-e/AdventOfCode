#!/usr/bin/env python3
f = open('input.txt', 'r')

X = 1
sol = 0
cycle = 0


def check_cycle():
    global sol
    if cycle in [20, 60, 100, 140, 180, 220]:
        sol += cycle*X


for line in f:
    if line.rstrip().split(' ')[0] == 'noop':
        cycle += 1
        check_cycle()
    else:
        cycle += 1
        check_cycle()
        cycle += 1
        check_cycle()
        X += int(line.rstrip().split(' ')[1])

print(sol)
