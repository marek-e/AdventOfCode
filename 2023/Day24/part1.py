f = open("input.txt", "r").read().strip()

res = 0
hailstones = []
for line in f.split("\n"):
    p, v = line.split(" @ ")
    p = list(map(int, p.split(", ")))
    v = list(map(int, v.split(", ")))
    hailstones.append((p, v))
n = len(hailstones)

for i in range(n):
    for j in range(i + 1, n):
        p_a, v_a = hailstones[i]
        p_b, v_b = hailstones[j]

        if v_b[0] * v_a[1] == v_b[1] * v_a[0]:  # prevent division by zero
            continue

        u = ((p_b[1] - p_a[1]) * v_b[0] - (p_b[0] - p_a[0]) * v_b[1]) / (
            v_b[0] * v_a[1] - v_b[1] * v_a[0]
        )
        v = ((p_b[1] - p_a[1]) * v_a[0] - (p_b[0] - p_a[0]) * v_a[1]) / (
            v_b[0] * v_a[1] - v_b[1] * v_a[0]
        )

        if u < 0 or v < 0:
            continue
        xi = p_b[0] + v_b[0] * v
        yi = p_b[1] + v_b[1] * v
        if (
            200000000000000 <= xi <= 400000000000000
            and 200000000000000 <= yi <= 400000000000000
        ):
            res += 1

print(res)
