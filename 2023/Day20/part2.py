f = open("input.txt", "r").read()


class Module:
    def __init__(self, line):
        name, dest = line.split(" -> ")
        if name == "broadcaster":
            self.name = name
            self.type = "B"
        else:
            self.name = name[1:]
            self.type = name[0]
        self.state = False
        self.dest = dest.split(", ")
        self.inputs = {}


class System:
    def __init__(self, input):
        self.modules = {m.name: m for m in map(Module, input.splitlines())}
        for empty in ("output", "rx"):
            self.modules[empty] = Module(empty + " -> ")
            self.modules[empty].dest = []
        for m in self.modules.values():
            for d in m.dest:
                self.modules[d].inputs[m.name] = False

        try:
            (self.parent,) = self.modules["rx"].inputs.keys()
            self.listen = {n: None for n in self.modules[self.parent].inputs.keys()}
        except ValueError:
            self.parent = None
            self.listen = {}

        self.Q = []
        self.pulses = [0, 0]
        self.buttonPresses = 0

    def buttonPress(self):
        self.buttonPresses += 1
        self.Q = [("button", "broadcaster", False)]
        while self.Q:
            self.process(*self.Q.pop(0))

    def process(self, source, name, level):
        self.pulses[level] += 1
        mod = self.modules[name]
        if mod.type == "%":
            if level:
                return
            mod.state = not mod.state
        elif mod.type == "&":
            mod.inputs[source] = level
            mod.state = not all(mod.inputs.values())
            if name == self.parent:
                for k, v in self.listen.items():
                    if v is None and k == source and level:
                        self.listen[k] = self.buttonPresses
        for d in mod.dest:
            self.Q.append((name, d, mod.state))

    def score2(self):
        ans = 1
        for v in self.listen.values():
            ans *= v
        return ans


s = System(f)

while None in s.listen.values():
    s.buttonPress()
print(s.score2())
