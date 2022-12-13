import math

data = []
INPUT_PATH: str = 'input'


# INPUT_PATH: str = 'sample2'


def read_data():
    global data
    with open(INPUT_PATH, 'r') as f:
        for line in f.readlines():
            data += [line.strip('\n')]


tail_pos = {}


class Knot(object):
    def __init__(self, x=0, y=0, parent=None):
        self.x = x
        self.y = y
        self.parent = parent

    def move(self, direction):
        match direction:
            case 'L':
                self.x -= 1
            case 'R':
                self.x += 1
            case 'D':
                self.y -= 1
            case 'U':
                self.y += 1
            case _:
                assert False
        if self.parent:
            self.parent.follow(self.x, self.y)
        else:
            tail_pos[self.x, self.y] = 1

    def follow(self, x, y):
        dist_x = x - self.x
        dist_y = y - self.y

        if dist_x > 1:
            self.x += 1
            if y > self.y:
                self.y += 1
            elif y < self.y:
                self.y -= 1
        elif dist_y > 1:
            self.y += 1
            if x > self.x:
                self.x += 1
            elif x < self.x:
                self.x -= 1
        elif dist_x < -1:
            self.x -= 1
            if y > self.y:
                self.y += 1
            elif y < self.y:
                self.y -= 1
        elif dist_y < -1:
            self.y -= 1
            if x > self.x:
                self.x += 1
            elif x < self.x:
                self.x -= 1

        if self.parent:
            self.parent.follow(self.x, self.y)
        else:
            tail_pos[self.x, self.y] = 1


def solution():
    tail_pos[0, 0] = 1
    tail = Knot(parent=None)
    head = tail
    for i in range(9):
        head = Knot(parent=head)

    for line in data:
        direction = line[0]
        length = int(line[2:])
        for mvmnt in range(length):
            head.move(direction)
    print(len(tail_pos))


def main():
    read_data()

    # global data

    solution()


if __name__ == '__main__':
    main()
