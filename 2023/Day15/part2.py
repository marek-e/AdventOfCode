from collections import defaultdict

f = open("input.txt", "r").read().split(",")


def hash(x: str) -> int:
    h = 0
    for c in x:
        h += ord(c)
        h = (17 * h) % 256
    return h


boxes = defaultdict(dict)

for step in f:
    if "-" in step:
        label = step.split("-")[0]
        boxes[hash(label)].pop(label, None)
    else:
        label, i = step.split("=")
        boxes[hash(label)][label] = int(i)

print(
    sum(
        sum((i + 1) * (j) * boxes[i][l] for j, l in enumerate(boxes[i], 1))
        for i in boxes
    ),
)
