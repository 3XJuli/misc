import math

data = []
INPUT_PATH: str = 'input'


# INPUT_PATH: str = 'sample'


def read_data():
    global data
    with open(INPUT_PATH, 'r') as f:
        for line in f.readlines():
            data += [line.strip('\n')]


def solution():
    total = 0
    X = 1
    dark = '.'
    lit = '#'
    draw_pos = 0
    cycle = 1

    sprite = [0, 2]
    drawing = ''

    for line in data:
        addx = line[:4] == 'addx'

        pixel = lit if (sprite[0] <= draw_pos <= sprite[1]) else dark

        drawing += pixel
        draw_pos += 1

        cycle += 1

        if cycle > 40:
            drawing += '\n'
            cycle = 1
            draw_pos = 0

        if addx:
            pixel = lit if (sprite[0] <= draw_pos <= sprite[1]) else dark
            drawing += pixel
            draw_pos += 1

            cycle += 1
            X += int(line[5:])
            sprite[0] += int(line[5:])
            sprite[1] += int(line[5:])

            if cycle > 40:
                drawing += '\n'
                cycle = 1
                draw_pos = 0

    print(drawing)

    return total


def main():
    read_data()

    # global data

    y = solution()
    print(y)


if __name__ == '__main__':
    main()
