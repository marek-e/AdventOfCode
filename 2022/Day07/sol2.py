from collections import defaultdict


class FileNode:
    def __init__(self, name, parent=None, size=0, is_dir=False):
        self.name = name
        self.parent = parent
        self.children = defaultdict(FileNode)
        self.size = size
        self.is_dir = is_dir

    def add_child(self, child):
        self.children[child.name] = child
        self.size += child.size
        curr = self
        while curr.parent:
            curr.parent.size += child.size
            curr = curr.parent

    def __iter__(self):
        yield self
        for child in self.children.values():
            yield from child

    def __setitem__(self, name, filenode):
        self.children[name] = filenode

    def __getitem__(self, name):
        return self.children[name]

    def __contains__(self, name):
        return name in self.children

    def __hash__(self):
        return hash(str(self.name) + str(self.parent))

    def __str__(self):
        return self.name

    def __repr__(self):
        return (
            f"FileNode({self.name}, parent={self.parent},"
            f" size={self.size}, is_dir={self.is_dir})"
        )


def build_filesystem():
    lines = open('input.txt').read().strip().splitlines()
    root = FileNode("/", None, 0, True)
    curr_dir = root
    for line in map(str.split, lines):
        if line[0] == "$":
            if line[1] == 'cd':
                path = line[2]
                if path == "/":
                    curr_dir = root
                elif path == ".." and curr_dir.parent:
                    curr_dir = curr_dir.parent
                elif path not in curr_dir:
                    dir = FileNode(path, curr_dir, 0, True)
                    curr_dir.add_child(dir)
                    curr_dir = dir
                else:
                    curr_dir = curr_dir[path]
        elif line[0] == "dir":
            dir = FileNode(line[1], curr_dir, 0, True)
            curr_dir.add_child(dir)
        else:
            size, file = line[0], line[1]
            file = FileNode(file, curr_dir, int(size), False)
            curr_dir.add_child(file)
    return root


root = build_filesystem()

# part 1)
p1_total = 0
for child in root:
    if child.is_dir and child.size <= 100000:
        p1_total += child.size
print(p1_total)

# part 2)
available = 70000000
update = 30000000
p2_dir = root
for child in root:
    if (
        child.is_dir
        and child.size > root.size + update - available
        and p2_dir.size > child.size
    ):
        p2_dir = child
print(p2_dir.size)
