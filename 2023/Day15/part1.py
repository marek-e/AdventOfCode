f = open("input.txt", "r").read().split(",")


def hash(x: str) -> int:
    h = 0
    for c in x:
        h += ord(c)
        h = (17 * h) % 256
    return h


print(sum([hash(x) for x in f]))
