f = open("input.txt", "r")

total = 0

t, d = [int("".join(l.split()[1:])) for l in f]

for i in range(1, t):
    if (t - i) * i > d:
        total += 1

print(total)
