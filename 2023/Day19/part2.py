from collections import deque


f = open("input.txt", "r")


def parse_rule(rule):
    label, rest = rule.split("{")
    return {label: rest[:-1].split(",")}


rules_str, _ = f.read().split("\n\n")
rules = {}
for r in rules_str.splitlines():
    rules.update(parse_rule(r))


MAX_RANGE = range(1, 4001)


class QuantumPart:
    def __init__(self, x=MAX_RANGE, m=MAX_RANGE, a=MAX_RANGE, s=MAX_RANGE) -> None:
        self.x = x
        self.m = m
        self.a = a
        self.s = s

    def copy(self):
        return QuantumPart(self.x, self.m, self.a, self.s)

    def apply_cond(self, xmas, comp, value):
        truthy = self.copy()
        falsy = self.copy()
        rating = getattr(self, xmas)
        if comp == ">":
            t = range(value + 1, rating.stop)
            f = range(rating.start, value + 1)
        elif comp == "<":
            t = range(rating.start, value)
            f = range(value, rating.stop)
        setattr(truthy, xmas, t)
        setattr(falsy, xmas, f)
        return truthy, falsy

    def __len__(self):
        return len(self.x) * len(self.m) * len(self.a) * len(self.s)


def quantum_workflow(rule: str, q_part):
    if rule == "A":
        return len(q_part)
    if rule == "R":
        return 0
    *conditions, default = rules[rule]
    total = 0
    for cond in conditions:
        cond, target = cond.split(":")
        cat = cond[0]
        comp = cond[1]
        val = int(cond[2:])
        t_part, q_part = q_part.apply_cond(cat, comp, val)
        total += quantum_workflow(target, t_part)
    return total + quantum_workflow(default, q_part)


print(quantum_workflow("in", QuantumPart()))
