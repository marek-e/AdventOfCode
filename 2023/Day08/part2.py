import math

f = open("input.txt", "r")

dirs, paths = f.read().split("\n\n")
paths = {
    k.strip(): v[2:-1].replace(" ", "").split(",")
    for k, v in (line.split("=") for line in paths.splitlines())
}
starts = [k for k in paths if k[-1] == "A"]
print(starts)


def steps_count(step):
    c = 0
    while step[-1] != "Z":
        d = dirs[c % len(dirs)]
        step = paths[step][d == "R"]
        c += 1
    return c


print(math.lcm(*map(steps_count, starts)))
