import math
from pprint import pprint
from dataclasses import dataclass, field
data = []
INPUT_PATH: str = 'input'
# INPUT_PATH: str = 'sample'

width: int = 7
total_rocks: int = 2022
total_rocks: int = 1000000000000

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
    down_border: int = 0
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
        self.upper_border = max([x[1] for x in self.coordinates])

    def set_length(self):
        self.n = len(self.coordinates)



rocks: dict[int, Rock] = dict()


def get_rocks():
    order = 4
    new_r = Rock(order)
    y = -1
    for line in reversed(rock_str.splitlines()):
        y += 1
        if not line:
            new_r.set()
            rocks[order] = new_r
            order -= 1
            y = -1
            new_r = Rock(order)

        else:
            x = 2
            for ch in line:
                if ch == '#':
                    new_r.coordinates.append((x, y))
                x+=1

    new_r.set()
    rocks[order] = new_r
    print(rocks)



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
    pprint(list(reversed(grid[:curr_height])))
    print(' [#, #, #, #, #, #, #]')
    print('\n')


def check_collision(grid: list[list[int]], pos: list[list[int]], movement: tuple[int, int]) -> bool:
    for x, y in pos:
        if (grid[y][x + movement[0]]) or (grid[y + movement[1]][x]):
            return True
    return False


def gust_move(grid: list[list[int]], pos: list[list[int]], gust_direction: int, l_e: int, r_e: int, n: int) -> tuple[int, int]:
    if gust_direction == -1 and (l_e + gust_direction < 0):
        pass
    elif gust_direction == 1 and (r_e + gust_direction > 6):
        pass
    else:
        if not check_collision(grid, pos, (gust_direction, 0)):
            for i in range(n):
                pos[i][0] += gust_direction
            l_e += gust_direction
            r_e += gust_direction
    return l_e, r_e

def down_move(grid: list[list[int]], pos: list[list[int]], d_e: int, u_e: int, n: int) -> tuple[int, int]:
    if d_e - 1 < 0:
        pass
    else:
        if not check_collision(grid, pos, (0, -1)):
            for i in range(n):
                pos[i][1] -= 1
            d_e -= 1
            u_e -= 1
    return d_e, u_e

@dataclass()
class Cycle(object):
    rock: Rock
    gust_ix: int
    distances_from_top: list[int] = field(default_factory=list)

    def update_distances_from_top(self, old_distances_from_top: list[int], old_height:int, new_height: int, rock_positions: list[list[int]]):
        new_height = max(old_height, new_height)
        if diff := new_height - old_height > 0:
            for i in range(len(old_distances_from_top)):
                old_distances_from_top[i] += diff
        for x, y in rock_positions:
            if new_height - y <= old_distances_from_top[x]:
                old_distances_from_top[x] = new_height - y
        self.distances_from_top = old_distances_from_top.copy()

    def __hash__(self):
        return hash((self.rock, self.gust_ix, *self.distances_from_top))
    def __eq__(self, other):
        return self.__hash__() == other.__hash__()



cycles: dict[Cycle, tuple[int, int]] = {}

def solution():
    global total_rocks
    global rocks
    global gust

    curr_max_height = 0
    gust_ix = 0
    differences_from_top = [1] * 7

    grid = [[0 for _ in range(7)] for _ in range(10000)]

    for r in range(total_rocks):
        order_rock = r % 5
        start_height = curr_max_height + 4 - 1
        curr_rock = rocks[order_rock]

        l_e = curr_rock.left_border
        r_e = curr_rock.right_border
        d_e = start_height
        u_e = curr_rock.upper_border + start_height

        curr_pos = [[x, y + start_height] for x, y in curr_rock.coordinates]

        while True:
            ## gust movement
            gust_direction = gust[gust_ix]
            l_e, r_e = gust_move(grid, curr_pos, gust_direction, l_e, r_e, curr_rock.n)

            # down_movement
            new_d_e, u_e = down_move(grid, curr_pos, d_e, u_e, curr_rock.n)

            if new_d_e == d_e:
                draw(grid, curr_pos, curr_rock.order)
                new_cycle = Cycle(curr_rock, gust_ix)
                new_cycle.update_distances_from_top(differences_from_top, curr_max_height, u_e + 1, curr_pos)
                if (new_height := (u_e + 1)) > curr_max_height:
                    curr_max_height = new_height

                if new_cycle in cycles:
                    cycle_start_r, cycle_start_h = cycles[new_cycle]
                    cycle_length = r - cycle_start_r
                    cycle_height = curr_max_height - cycle_start_h

                    cycles_total = (total_rocks - cycle_start_r - 1) // cycle_length
                    length_remaining = (total_rocks - cycle_start_r - 1) % cycle_length

                    remainder_cycle_height = 0
                    for rem, height in cycles.values():
                        if rem == (cycle_start_r + length_remaining):
                            remainder_cycle_height = height

                    print(cycles_total * cycle_height + remainder_cycle_height)
                    print('cycle found')

                cycles[new_cycle] = r, curr_max_height




                gust_ix += 1
                gust_ix %= len(gust)
                break
            else:
                gust_ix += 1
                gust_ix %= len(gust)
                d_e = new_d_e

        if r == 100: _cout(grid, curr_max_height)
    print(curr_max_height)












def main():
    read_data()
    get_rocks()
    parse_gust()

    solution()


if __name__ == '__main__':
    main()
