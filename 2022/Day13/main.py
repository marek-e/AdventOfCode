#!/usr/bin/env python3
from functools import cmp_to_key


f = open('input.txt', 'r')
pairs = [list(map(eval, x.splitlines())) for x in f.read().split('\n\n')]


def compare(left, right):
    if not isinstance(left, list):
        left = [left]
    if not isinstance(right, list):
        right = [right]
    for l, r in zip(left, right):
        if isinstance(l, list) or isinstance(r, list):
            res = compare(l, r)
        else:
            res = r - l
        if res != 0:
            return res
    return len(right) - len(left)


part1 = sum(i for i, (left, right) in enumerate(pairs, 1)
            if compare(left, right) > 0)
print(part1)

part2 = 1
sorted_list = sorted([y for x in pairs for y in x] + [[[2]], [[6]]],
                     key=cmp_to_key(compare), reverse=True)
for i, item in enumerate(sorted_list, 1):
    if item in ([[2]], [[6]]):
        part2 *= i

print(part2)
