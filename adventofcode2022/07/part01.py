import math

data = []
INPUT_PATH: str = 'input'

output: int = 0


class Node:
    files: dict[str, int] = {}

    def __init__(self, name, parent, children):
        self.name = name
        self.parent = parent
        self.children = children
        self.files = {}

    def get_size(self):
        cost = 0
        for child in self.children.values():
            cost += child.get_size()
        cost += sum(self.files.values()) if self.files else 0
        if cost <= 100000:
            global output
            output = output + cost
        return cost


def read_data():
    global data
    with open(INPUT_PATH, 'r') as f:
        for line in f.readlines():
            data += [line.strip('\n')]


def solution():
    total = 0
    global data
    root_node: Node = Node('/', None, {})
    current_directory: Node = root_node
    for ix, line in enumerate(data):
        if line[0] == '$':
            if line[2:4] == 'cd':
                if line[5:] == '..':
                    current_directory = current_directory.parent
                elif line[5:] == '/':
                    current_directory = root_node
                else:
                    node_name = line[5:]
                    if node_name not in current_directory.children:
                        current_directory.children[node_name] = Node(node_name, current_directory, {})
                    current_directory = current_directory.children[node_name]
        else:
            if line[0] == 'd':
                if line[4:] not in current_directory.children:
                    current_directory.children[line[4:]] = Node(line[4:], current_directory, {})
            else:
                file_size, file_name = line.split(' ')
                current_directory.files[file_name] = int(file_size)
    root_node.get_size()
    global output
    print(output)


def main():
    read_data()

    # global data

    solution()


if __name__ == '__main__':
    main()
