from functools import lru_cache

f = open("input.txt", "r")


@lru_cache
def nb_arrangements(pixels: str, groups: tuple[int]):
    if len(pixels) == 0:
        return 1 if len(groups) == 0 else 0
    if pixels.startswith("."):
        return nb_arrangements(pixels.strip("."), groups)
    if pixels.startswith("?"):
        return nb_arrangements(pixels.replace("?", ".", 1), groups) + nb_arrangements(
            pixels.replace("?", "#", 1), groups
        )
    if pixels.startswith("#"):
        if len(groups) == 0:
            return 0
        if len(pixels) < groups[0]:
            return 0
        if any(c == "." for c in pixels[0 : groups[0]]):
            return 0
        if len(groups) > 1:
            if len(pixels) < groups[0] + 1 or pixels[groups[0]] == "#":
                return 0
            return nb_arrangements(pixels[groups[0] + 1 :], groups[1:])
        else:  # len(groups) == 1
            return nb_arrangements(pixels[groups[0] :], groups[1:])


total = 0
for line in f:
    row, config = line.strip().split()
    config = tuple([int(k) for k in config.split(",")] * 5)
    row = "?".join([row] * 5)
    total += nb_arrangements(row, config)

print(total)
