import math
from pprint import pprint
from dataclasses import dataclass, field
data = []
INPUT_PATH: str = 'input'
INPUT_PATH: str = 'sample'

width: int = 7
total_rocks: int = 1_000_000_000_000

rock_str: str = """####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##
"""

def read_data():
    global data
    with open(INPUT_PATH, 'r') as f:
        for line in f.readlines():
            data += [line.strip('\n')]

@dataclass()
class Rock(object):
    order: int
    right_border: int = -1
    left_border: int = -1
    down_border: int = -1
    upper_border: int = -1
    n: int = -1
    coordinates: list[tuple[int, int]] = field(default_factory=list)


    def __hash__(self):
        return hash(self.order)

    def set(self):
        self.set_borders()
        self.set_length()

    def set_borders(self):
        self.left_border = min([x[0] for x in self.coordinates])
        self.right_border = max([x[0] for x in self.coordinates])
        self.down_border = min([x[1] for x in self.coordinates])
        self.upper_border = 0

    def set_length(self):
        self.n = len(self.coordinates)



rocks: dict[int, Rock] = dict()


def get_rocks():
    order = 0
    new_r = Rock(order)
    y = 0
    for line in rock_str.splitlines():
        if not line:
            new_r.set()
            rocks[order] = new_r
            order += 1
            y = 1
            new_r = Rock(order)

        else:
            x = 2
            for ch in line:


                if ch == '#':
                    new_r.coordinates.append((x, y))

                x+=1
        y -= 1

    new_r.set()
    rocks[order] = new_r
    order += 1



gust: tuple
def parse_gust():
    g = list()
    global gust
    for ch in data[0]:
        if ch == '<':
            g.append(-1)
        if ch == '>':
            g.append(1)
    gust = tuple(g)

def resize():
    pass

def draw(grid: list[list[int]], pos: list[list[int]], order=1):
    for x, y in pos:
        grid[y][x] = order + 1


def _cout(grid, curr_height, height = 10):
    n = len(grid)
    pprint(grid[-n + curr_height: -n+ curr_height -height: -1])
    print(' [#, #, #, #, #, #, #]')
    print('\n')


def check_collision(grid: list[list[int]], pos: list[list[int]], movement: tuple[int, int]) -> bool:
    for x, y in pos:
        if (grid[y][x + movement[0]]) or (grid[y + movement[1]][x]):
            return True
    return False


def update_pos_x(grid: list[list[int]], pos: list[list[int]], movement_x: int, l_e: int, r_e: int, n: int) -> tuple[int, int]:
    if movement_x == -1 and (l_e + movement_x < 0):
        pass
    elif movement_x == 1 and (r_e + movement_x > 6):
        pass
    else:
        if not check_collision(grid, pos, (movement_x, 0)):
            for i in range(n):
                pos[i][0] += movement_x
            l_e += movement_x
            r_e += movement_x
    return l_e, r_e

def update_pos_y(grid: list[list[int]], pos: list[list[int]], d_e: int, u_e: int, n: int) -> tuple[int, int]:
    if d_e - 1 < 0:
        pass
    else:
        if not check_collision(grid, pos, (0, -1)):
            for i in range(n):
                pos[i][1] -= 1
            d_e -= 1
            u_e -= 1
    return d_e, u_e

# needs to be relative to new heighest point
def update_distance_from_top(distance_from_top: list[int], pos: list[list[int]], diff: int, curr_height: int):
    for i in range(len(distance_from_top)):
        distance_from_top[i] += diff

    for x, y in pos:
        if distance_from_top[x] > curr_height - y:
            distance_from_top[x] = curr_height - y



cycles: dict[tuple[int, tuple[int]], int] = {}

def solution():
    global total_rocks
    global rocks
    global gust
    global cycles

    len_rocks = len(rocks)
    len_gust = len(gust)

    curr_max_height = 0
    gust_ix = 0
    distance_from_top = [1] * 7
    grid = [[0 for i in range(7)] for j in range(1_000_000)]
    for r in range(total_rocks):
        if r >= 100000-1:
            break
        order_rock = r % 5

        # print(cycles)
        start_height = curr_max_height + 3
        curr_rock = rocks[order_rock]

        l_e = curr_rock.left_border
        r_e = curr_rock.right_border
        d_e = start_height
        u_e = abs(curr_rock.down_border) + start_height

        curr_pos = [[x, y + u_e] for x, y in curr_rock.coordinates]




        while True:
            ## gust movement
            movement_x = gust[gust_ix]
            l_e, r_e = update_pos_x(grid, curr_pos, movement_x, l_e, r_e, curr_rock.n)
            new_d_e, u_e = update_pos_y(grid, curr_pos, d_e, u_e, curr_rock.n)
            gust_ix += 1
            gust_ix %= len(gust)
            if new_d_e == d_e:

                draw(grid, curr_pos, curr_rock.order)

                if u_e >= curr_max_height:
                    diff = u_e + 1 - curr_max_height
                    curr_max_height = u_e + 1
                    update_distance_from_top(distance_from_top, curr_pos, diff, curr_max_height)


                break

            else:
                d_e = new_d_e
        # _cout(grid, curr_max_height)

        if (order_rock, tuple(distance_from_top)) in cycles:
            old_r, old_max_height =  cycles[order_rock, tuple(distance_from_top)]
            difference_in_heights = curr_max_height - old_max_height
            r_diff = r - old_r

            contained_cycles = (total_rocks - old_r) // r_diff
            remaining_cycles = (total_rocks - old_r) % r_diff

            # rock_n // old_r *

            remainder_cycle_height = None
            for r, height in cycles.values():
                if r == (old_r + remaining_cycles + 1):
                    remainder_cycle_height = height
                    break

            curr_max_height = (contained_cycles * difference_in_heights) + remainder_cycle_height
            print('cycle found')
            break
        cycles[order_rock, tuple(distance_from_top)] = (r, curr_max_height)
    print(curr_max_height)












def main():
    read_data()
    get_rocks()
    parse_gust()

    solution()


if __name__ == '__main__':
    main()
