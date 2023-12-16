config = {
    x + y * 1j: col
    for y, row in enumerate(open("input.txt"))
    for x, col in enumerate(row.strip())
}


def count(todo: set):
    done = set()
    while todo:
        p, d = todo.pop()
        while not (p, d) in done:
            done.add((p, d))
            p += d
            match config.get(p):
                case "\\":
                    d = (d * -1j).conjugate()
                case "/":
                    d = (d * 1j).conjugate()
                case "|":
                    d = 1j
                    todo.add((p, -1j))
                case "-":
                    d = 1
                    todo.add((p, -1))
                case None:
                    break

    return len(set(x for x, _ in done)) - 1


print(
    max(
        map(
            count,
            (
                {((p - d, d))}
                for p in config
                for d in (1, 1j, -1, -1j)  # all 4 directions
                if p - d not in config
            ),
        )
    )
)
