import math

data = []
INPUT_PATH: str = 'input'


# INPUT_PATH: str = 'sample'


def read_data():
    global data
    with open(INPUT_PATH, 'r') as f:
        for line in f.readlines():
            data += [line.strip('\n')]


def plot(visited: set):
    print('####################')
    x = ''
    for iy, line in enumerate(data):
        for ix, ch in enumerate(line):
            if (iy, ix) in visited:
                x += ch
            else:
                x += ' '
        print(x)
        x = ''
    print('####################')


class Node(object):
    def __init__(self, x: int, y: int, letter: int, length: int = 0):
        self.x = x
        self.y = y
        self.length = length
        self.visited = False
        self.letter = letter

    def __key(self):
        return self.x, self.y

    def __hash__(self):
        return hash(self.__key())

    def __lt__(self, other):
        return self.length < other.length

    def __eq__(self, other):
        return self.__key() == other.__key()

    def __repr__(self):
        return str(self.__dict__)


class Dijkstra(object):
    data: list[str] = []
    nodes: set[Node] = set()
    n: int
    m: int
    s: Node
    e: Node
    int_set: set

    def __init__(self, data: list[str]):
        self.data = data.copy()
        self.n = len(data[0]) - 1
        self.m = len(data) - 1

    @staticmethod
    def get_pos(some_ch: chr) -> tuple[int, int]:
        for row, line in enumerate(data):
            for col, ch in enumerate(line):
                if ch == some_ch:
                    return col, row

    def find_path_start_to_end(self, start_char: chr, end_char: chr):
        self.s = Node(*self.get_pos(start_char), ord('a'), 0)
        self.e = Node(*self.get_pos(end_char), ord(end_char), -1)

        self.nodes.add(self.s)

        self.int_set: set = {self.s}
        node = self.s
        while node != self.e:

            node: Node = min(self.int_set)
            # self.nodes.remove(node)
            node.visited = True
            self.int_set.remove(node)
            self.find_neighbors(node)
        return node.length

    def add_neighbor(self, x: int, y: int, node: Node):
        new_node = Node(x, y, ord(data[y][x]), node.length + 1)
        if new_node == self.e:
            new_node.letter = ord('z')
        if new_node.letter - node.letter <= 1 and new_node not in self.nodes:
            self.nodes.add(new_node)
            self.int_set.add(new_node)

    def find_neighbors(self, node: Node):
        node_x, node_y = node.x, node.y
        if node_x > 0:
            self.add_neighbor(node_x - 1, node_y, node)
        if node_y > 0:
            self.add_neighbor(node_x, node_y - 1, node)
        if node_x < self.n:
            self.add_neighbor(node_x + 1, node_y, node)
        if node_y < self.m:
            self.add_neighbor(node_x, node_y + 1, node)

    def find_path_end_to_char(self, start_char: chr, end_char: chr):
        pass


def solution():
    dijk = Dijkstra(data)

    length = dijk.find_path_start_to_end('S', 'E')
    print(length)


def main():
    read_data()

    # global data

    solution()


if __name__ == '__main__':
    main()
