f = open("input.txt", "r")


def parse_rule(rule):
    label, rest = rule.split("{")
    return {label: rest[:-1].split(",")}


def parse_part(part):
    return eval(f"dict({part[1:-1]})")


rules_str, parts_str = f.read().split("\n\n")
rules = {}
for r in rules_str.splitlines():
    rules.update(parse_rule(r))
parts = list(map(parse_part, parts_str.splitlines()))


def isWorkflowAccepted(rule: str, part):
    if rule == "A":
        return True
    if rule == "R":
        return False
    *conditions, default = rules[rule]
    for cond in conditions:
        cond, target = cond.split(":")
        cat = cond[0]
        op = cond[1]
        val = int(cond[2:])
        if op == "<":
            if part[cat] < val:
                return isWorkflowAccepted(target, part)
        if op == ">":
            if part[cat] > val:
                return isWorkflowAccepted(target, part)
    return isWorkflowAccepted(default, part)


print(sum(sum(p.values()) for p in parts if isWorkflowAccepted("in", p)))
