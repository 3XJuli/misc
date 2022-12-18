import math
import sys
from typing import Optional
from pprint import pprint

import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

data = []
INPUT_PATH: str = 'input'
# INPUT_PATH: str = 'sample'


sys.setrecursionlimit(10000)


def read_data():
    global data
    with open(INPUT_PATH, 'r') as f:
        for line in f.readlines():
            data += [line.strip('\n')]


# x, y, z
points: list[tuple[int, int, int]] = []


class Bubble(object):

    def __init__(self, x: int, y: int, z: int, n_x: int, n_y: int, n_z: int):
        self.n_x = n_x
        self.n_y = n_y
        self.n_z = n_z
        self.seen_closed_borders = 0
        self.start_point = (x, y, z)
        self.contained_points = set()
        self.inner_bubble = True

    def __hash__(self):
        return hash(self.start_point)

    def __repr__(self):
        return f'Start-point: {self.start_point}; Contained-Points: {self.contained_points}'

    def explore(self, point: Optional[tuple[int, int, int]] = None, depth: int = 0) -> bool:
        global seen_points

        if not point:
            x, y, z = self.start_point
        else:
            x, y, z = point

        seen_points[x, y, z] = self
        self.contained_points.add((x, y, z))

        # loop -1, 1
        for i in range(2):
            j = 1 + (i * -2)
            if 0 <= x + j < self.n_x:
                if grid[x + j][y][z]:
                    self.seen_closed_borders += 1
                elif (x + j, y, z) not in seen_points:
                    if 0 == x + j or self.n_x - 1 == x + j:
                        self.inner_bubble = False
                    else:
                        self.explore((x + j, y, z), depth=depth + 1)
            if 0 <= y + j < self.n_y:
                if grid[x][y + j][z]:
                    self.seen_closed_borders += 1
                elif (x, y + j, z) not in seen_points:
                    if 0 == y + j or self.n_y - 1 == y + j:
                        self.inner_bubble = False
                    else:
                        self.explore((x, y + j, z), depth=depth + 1)

            if 0 <= z + j < self.n_z:
                if grid[x][y][z + j]:
                    self.seen_closed_borders += 1
                elif (x, y, z + j) not in seen_points:
                    if 0 == z + j or self.n_z - 1 == z + j:
                        self.inner_bubble = False
                    else:
                        self.explore((x, y, z + j), depth=depth + 1)
        return True


seen_points: dict[tuple[int, int, int], Bubble] = {}


def parse():
    global data
    for line in data:
        x, y, z = line.split(',')
        x = int(x)
        y = int(y)
        z = int(z)
        points.append((x, y, z))


def get_grid_size():
    xmax = ymax = zmax = 0
    for x, y, z in points:
        xmax = max(xmax, x)
        ymax = max(ymax, y)
        zmax = max(zmax, z)

    return xmax + 1, ymax + 1, zmax + 1

exposed_side: dict[tuple[int, int, int]] = {}
grid: list[list[list[int]]] = []
bubbles: list[Bubble] = []


def plot():
    global grid
    fig = plt.figure()
    ax = plt.axes(projection='3d')

    xdata = []
    ydata = []
    zdata = []
    for x, y, z in points:
        xdata.append(x)
        ydata.append(y)
        zdata.append(z)

    ax.scatter(xdata, ydata, zdata, 'gray')
    # ax.scatter(2, 2, 5, 'red')
    plt.show()


def solution():
    global exposed_side
    global grid
    global seen_points

    n_x, n_y, n_z = get_grid_size()
    grid = [[[0 for k in range(n_z)] for j in range(n_y)] for i in range(n_x)]
    # plot()

    for point in points:
        x, y, z = point

        grid[x][y][z] = 1
        exposed_side_count = 6

        for i in range(2):
            j = 1 + (i * -2)
            if 0 <= x + j < n_x and grid[x + j][y][z]:
                exposed_side[x + j, y, z] = max(exposed_side[x + j, y, z] - 1, 0)
                exposed_side_count -= 1
            if 0 <= y + j < n_y and grid[x][y + j][z]:
                exposed_side[x, y + j, z] = max(exposed_side[x, y + j, z] - 1, 0)
                exposed_side_count -= 1
            if 0 <= z + j < n_z and grid[x][y][z + j]:
                exposed_side[x, y, z + j] = max(exposed_side[x, y, z + j] - 1, 0)
                exposed_side_count -= 1
        exposed_side[x, y, z] = exposed_side_count

    for x in range(1, n_x - 1):
        for y in range(2, n_y - 1):
            for z in range(1, n_z - 1):
                if not grid[x][y][z] and (x, y, z) not in seen_points:

                    new_bubble = Bubble(x, y, z, n_x, n_y, n_z)
                    new_bubble.explore()
                    if new_bubble.inner_bubble:
                        bubbles.append(new_bubble)
    # pprint(bubbles)
    print(sum([v for v in exposed_side.values()]) - sum([bubble.seen_closed_borders for bubble in bubbles]))


def main():
    read_data()
    parse()

    solution()


if __name__ == '__main__':
    main()
