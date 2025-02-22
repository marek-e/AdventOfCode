almanac = open("input.txt", "r")

almanac = almanac.read().split("\n")

seeds = []
i = 0
start = 0
for elem in [int(k) for k in almanac[0].split(" ")[1:]]:
    if i == 0:
        start = elem
        i += 1
    elif i == 1:
        seeds += list(range(start, start + elem))
        i = 0

len_maps = 7

maps = [[] for i in range(len_maps)]
i = -1
for line in almanac[1:]:
    if line == "":
        continue
    if "map:" in line:
        i += 1
        continue
    maps[i].append([int(k) for k in line.split(" ")])

locations = []

for n in seeds:
    for map in maps:
        for line in map:
            if line[1] <= n <= line[1] + line[2] - 1:
                n = n - line[1] + line[0]
                break
    locations.append(n)

print(min(locations))
