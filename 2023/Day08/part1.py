f = open("input.txt", "r")

dirs, paths = f.read().split("\n\n")
paths = {
    k.strip(): v[2:-1].replace(" ", "").split(",")
    for k, v in (line.split("=") for line in paths.splitlines())
}


def steps(s):
    c = 0
    while s != "ZZZ":
        d = dirs[c % len(dirs)]
        s = paths[s][d == "R"]
        c += 1
    return c


print(steps("AAA"))
