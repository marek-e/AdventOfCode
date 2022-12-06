#!/usr/bin/env python3
f = open('input.txt', 'r')

line = f.readline()
cur_packet = list(line[:14])


def has_duplicate(l):
    return len(set(l)) < len(l)


for i in range(14, len(line)):
    cur_packet.pop(0)
    cur_packet.append(line[i])
    if not has_duplicate(cur_packet):
        print(i+1)
        break
