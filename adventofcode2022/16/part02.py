import math
from typing import Optional

data = []
INPUT_PATH: str = 'input'


# INPUT_PATH: str = 'sample1'


class Node(object):
    def __init__(self, node_name: str, flow_rate: int = -1, edges: list[str] = None):
        self.node_name = node_name
        self.edges = edges
        self.flow_rate = flow_rate
        self.activated = False

    def __hash__(self):
        return hash(self.node_name)

    def __eq__(self, other):
        return self.node_name == other.node_name

    def __repr__(self):
        return f'node: {self.node_name}' \
            # f', flow_rate: {self.flow_rate},edges: {", ".join([e.node_name for e in self.edges])} }}'


nodes: dict[str, Node] = {}


def read_data():
    global data
    with open(INPUT_PATH, 'r') as f:
        for line in f.readlines():
            data += [line.strip('\n')]


AA: Optional[Node] = None


def parse():
    global data
    global nodes
    global AA
    for line in data:

        node_name = line[6:8]
        if node_name in nodes:
            main_node = nodes[node_name]
        else:
            main_node = Node(node_name)
            nodes[node_name] = main_node

        fr, edg = line[23:].split(';')
        main_node.flow_rate = int(fr)

        if node_name == 'AA':
            AA = main_node
            AA.activated = 1
        edges = list()
        split_valve = edg.split('valve')[1]
        if split_valve[0] == 's':
            split_valve = split_valve[1:]
        split_valve = split_valve[1:]
        for o_node in split_valve.split(', '):
            if o_node in nodes:
                n_node = nodes[o_node]
            else:
                n_node = Node(o_node)
                nodes[o_node] = n_node

            edges.append(n_node)
        main_node.edges = edges


distances: dict[tuple[nodes, nodes], int] = {}


def calc_distances():
    global distances
    for node1 in nodes.values():
        for node2 in node1.edges:
            distances[node1, node2] = 1
    n = len(nodes.keys())
    for node_between in nodes.values():
        for node1 in nodes.values():
            for node2 in nodes.values():
                if node1 == node2:
                    distances[node1, node2] = 0
                if (node1, node_between) in distances and (node2, node_between) in distances:
                    if (node1, node2) not in distances or distances[node1, node2] > (
                            distances[node1, node_between] + distances[node2, node_between]):
                        distances[node1, node2] = distances[node1, node_between] + distances[node2, node_between]
    print(distances)


def distance_sum(node: Node) -> int:
    dist_sum: int = 0
    for k, distance in distances.items():
        if k[0] == node and not k[1].activated:
            dist_sum += distance
    return dist_sum


max_w: int = 26


def recursion(curr_weight: int, curr_node: Node, curr_path, remaining: list[Node]):
    max_new_value = 0
    for node in remaining:
        dist = distances[curr_node, node]
        new_weight = curr_weight + dist + 1
        new_value = 0

        if new_weight == 26:
            new_value = (max_w - new_weight) * node.flow_rate
        elif new_weight < 26:
            # recursion
            new_curr_path = curr_path + [node]
            new_remaining = remaining.copy()
            new_remaining.remove(node)
            new_value = (max_w - new_weight) * node.flow_rate + recursion(new_weight, node, new_curr_path,
                                                                          new_remaining)

        if new_value > max_new_value:
            max_new_value = new_value

    return max_new_value

cache: dict[tuple[int, int, Node, Node, tuple[Node]]] = {}


def recursion2(curr_lweight: int,
               curr_rweight: int,
               lcurr_node: Node,
               rcurr_node: Node,
               lcurr_path: list[Node],
               rcurr_path: list[Node],
               remaining: list[Node]
               # root=False
               ):
    if not remaining:
        return 0
    max_new_value = 0

    tuple_remaining: tuple[Node] = tuple(remaining)
    if (curr_lweight, curr_rweight, lcurr_node, rcurr_node, tuple_remaining) in cache:
        # print('hit')
        return cache[curr_lweight, curr_rweight, lcurr_node, rcurr_node, tuple_remaining]


    for i1, node1 in enumerate(remaining):
        for i2, node2 in enumerate(remaining):
            if node1 == node2:
                continue
            dist1 = distances[lcurr_node, node1]
            dist2 = distances[rcurr_node, node2]
            lweight = curr_lweight + dist1 + 1
            rweight = curr_rweight + dist2 + 1
            new_value = 0

            l_value = (max_w - lweight) * node1.flow_rate
            r_value = (max_w - rweight) * node2.flow_rate

            new_remaining = remaining.copy()
            if lweight <= max_w:
                new_value += l_value
                new_remaining.remove(node1)
            if rweight <= max_w:
                new_value += r_value
                new_remaining.remove(node2)

            new_lpath = lcurr_path + [node1]
            new_rpath = rcurr_path + [node2]

            if lweight < max_w and rweight < max_w:
                new_value += recursion2(lweight, rweight, node1, node2, new_lpath, new_rpath, new_remaining)
            elif lweight < max_w:
                new_value += recursion(lweight, node1, new_lpath, new_remaining)
            elif rweight < max_w:
                new_value += recursion(rweight, node2, new_rpath, new_remaining)

            if new_value > max_new_value:
                max_new_value = new_value
    cache[curr_lweight, curr_rweight, lcurr_node, rcurr_node, tuple_remaining] = max_new_value
    return max_new_value


def solution():
    import time
    start_time = time.time()
    print(start_time)
    init_node = AA
    curr_path = [AA]
    remaining = [node for node in nodes.values() if node != AA and node.flow_rate > 0]
    y = recursion2(0, 0, AA, AA, curr_path, curr_path, remaining)
    print(y)
    print(time.time() - start_time)


def main():
    read_data()
    parse()
    calc_distances()

    solution()


if __name__ == '__main__':
    main()
