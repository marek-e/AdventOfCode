#!/usr/bin/env python3
f = open('input.txt', 'r')

X = 1
sol = []  # CRT row
for _ in range(6):
    sol.append('')
i = 0
cycle = 0


def check_cycle():
    global sol, i
    if cycle in [41, 81, 121, 161, 201]:
        i += 1
    if X <= cycle - i*40 <= X + 2:
        sol[i] += '#'
    else:
        sol[i] += ' '


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


for row in sol:
    print(row)
