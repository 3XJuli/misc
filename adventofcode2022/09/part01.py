import math

data = []
INPUT_PATH: str = 'input'
# INPUT_PATH: str = 'sample1'


def read_data():
    global data
    with open(INPUT_PATH, 'r') as f:
        for line in f.readlines():
            data += [line.strip('\n')]


tail_pos = {}


def solution():
    tx = ty = hx = hy = 0
    tail_pos[tx, ty] = 1
    for line in data:
        dir = line[0]
        length = int(line[2:])
        for mvmnt in range(length):
            match dir:
                case 'L':
                    hx -= 1
                case 'R':
                    hx += 1
                case 'D':
                    hy -= 1
                case 'U':
                    hy += 1
                case _:
                    assert False

            dist_x = hx - tx
            dist_y = hy - ty
            if dist_x > 1:
                tx += 1
                if hy > ty:
                    ty += 1
                elif hy < ty:
                    ty -= 1
            elif dist_y > 1:
                ty += 1
                if hx > tx:
                    tx += 1
                elif hx < tx:
                    tx -= 1
            elif dist_x < -1:
                tx -= 1
                if hy > ty:
                    ty += 1
                elif hy < ty:
                    ty -= 1
            elif dist_y < -1:
                ty -= 1
                if hx > tx:
                    tx += 1
                elif hx < tx:
                    tx -= 1
            print("HEAD:", hx, hy)
            print("TAIL:", tx, ty)
            print("----")
            tail_pos[tx, ty] = 1
    print(len(tail_pos))

def main():
    read_data()

    # global data

    solution()


if __name__ == '__main__':
    main()
