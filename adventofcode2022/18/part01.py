import math

import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

data = []
INPUT_PATH: str = 'input'
INPUT_PATH: str = 'sample'


def read_data():
    global data
    with open(INPUT_PATH, 'r') as f:
        for line in f.readlines():
            data += [line.strip('\n')]

# x, y, z
points: list[tuple[int, int ,int]] = []

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
    return xmax+1, ymax+1, zmax+1

exposed_side: dict[tuple[int, int, int]] = {}
grid: list[list[list[int]]] = []

def plot(nx, ny, nz):
    global grid
    fig = plt.figure()
    ax = plt.axes(projection = '3d')

    xdata = []
    ydata = []
    zdata = []
    for x, y, z in points:
        xdata.append(x)
        ydata.append(y)
        zdata.append(z)

    ax.scatter(xdata, ydata, zdata, 'gray')
    ax.scatter(2, 2, 5, 'red')
    plt.show()

def solution():
    global exposed_side
    global grid
    n_x, n_y, n_z = get_grid_size()
    grid = [[[0 for k in range(n_z)] for j in range(n_y) ]for i in range(n_x)]
    plot(n_x, n_y, n_z)

    for point in points:
        x, y, z = point
        try:
            assert not grid[x][y][z]
        except IndexError as e:
            print('debug')

        grid[x][y][z] = 1
        exposed_side_count = 6

        for i in range(2):
            j = 1 + (i * -2)
            if 0 <= x+j < n_x and grid[x + j][y][z]:
                exposed_side[x +j, y, z] = max(exposed_side[x +j, y, z] - 1, 0)
                exposed_side_count -= 1
            if 0 <= y+j < n_y and grid[x][y + j][z]:
                exposed_side[x, y+j, z] = max(exposed_side[x, y+j, z] - 1, 0)
                exposed_side_count -= 1
            if 0 <= z+j < n_z  and grid[x][y][z + j]:
                exposed_side[x, y, z+j] = max(exposed_side[x, y, z+j] - 1, 0)
                exposed_side_count -= 1
        exposed_side[x, y, z] = exposed_side_count

    print(sum([v for v in exposed_side.values()]))






def main():
    read_data()
    parse()

    # global data

    solution()


if __name__ == '__main__':
    main()
