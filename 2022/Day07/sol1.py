def sizes(lines):
    s = []  # accumulator
    R = []  # sizes emitted
    for line in lines:
        tok = line.split(" ")
        if tok[0] == "$":  # command
            if tok[1] == "cd":
                if tok[2] == "..":  # emit cur size and add to upper dir
                    R.append(s.pop())
                    s[-1] += R[-1]
                else:  # enter new dir
                    s.append(0)
        elif tok[0] != "dir":  # output
            s[-1] += int(tok[0])
    return R + list(accumulate(reversed(s)))


def part1(lines):
    return sum(filter(lambda x: x <= 100000, sizes(lines)))


def part2(lines):
    R = sizes(lines)
    available = 70000000-R[-1]
    return min(filter(lambda x: x+available >= 30000000, R))
