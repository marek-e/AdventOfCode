f = open("input.txt", "r")

total = 1

t, d = [l.split()[1:] for l in f]
t = [int(time) for time in t]
d = [int(dist) for dist in d]

for k, time in enumerate(t):
    count = 0
    for i in range(1, time):
        if (time - i) * i > d[k]:
            count += 1
    total *= count

print(total)
