f = open("input.txt", "r")

total = 0


def extrapolate(line) -> int:
    l = [int(x) for x in line]
    n = l[-1]
    while sum(i != 0 for i in l) != 0:
        tmp = []
        for i in range(len(l) - 1):
            tmp.append(l[i + 1] - l[i])
        l = tmp
        n += l[-1]

    return n


for line in f:
    total += extrapolate(line.strip().split(" ")[::-1])
print(total)
