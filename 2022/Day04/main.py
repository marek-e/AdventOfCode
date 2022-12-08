f = open("input.txt", "r")

n = 0
n2 = 0

for line in f:
    p = line.rstrip().split(',')
    a1 = p[0].split('-')
    a2 = p[1].split('-')
    s1 = set(range(int(a1[0]), int(a1[1])+1))
    s2 = set(range(int(a2[0]), int(a2[1])+1))

    if s1.issubset(s2) or s2.issubset(s1):
        n += 1

    if not s1.isdisjoint(s2) or not s2.isdisjoint(s1):
        n2 += 1


print(n)
print(n2)
