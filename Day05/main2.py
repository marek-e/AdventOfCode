#!/usr/bin/env python3
f = open('input.txt', 'r')


STACKS = {
    1: ['B', 'W', 'N'],
    2: ['L', 'Z', 'S', 'P', 'T', 'D', 'M', 'B'],
    3: ['Q', 'H', 'Z', 'W', 'R'],
    4: ['W', 'D', 'V', 'J', 'Z', 'R'],
    5: ['S', 'H', 'M', 'B'],
    6: ['L', 'G', 'N', 'J', 'H', 'V', 'P', 'B'],
    7: ['J', 'Q', 'Z', 'F', 'H', 'D', 'L', 'S'],
    8: ['W', 'S', 'F', 'J', 'G', 'Q', 'B'],
    9: ['Z', 'W', 'M', 'S', 'C', 'D', 'J'],
}

for line in f:
    l = line.split(' ')
    if l[0] == 'move':
        elem = STACKS[int(l[3])][-int(l[1]):]
        STACKS[int(l[3])] = STACKS[int(l[3])][:-int(l[1])]
        for e in elem:
            STACKS[int(l[5])].append(e)

sol = ''
for j in range(len(STACKS)):
    sol += STACKS[j+1][-1]
print(sol)
