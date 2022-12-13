import math

data = []
INPUT_PATH: str = 'input'


def read_data():
    global data
    with open(INPUT_PATH, 'r') as f:
        for line in f.readlines():
            data += [line.strip('\n')]


def solution():
    crates = [[]] * 9
    for line in data[:8]:
        i = 0
        ix = 0
        while i < len(line):
            if line[i:(i+3)] != '   ':
                crates[ix] = crates[ix] + [line[i+1]]
            ix += 1
            i += 4
    for line in data[10:]:
        cnt, von, zu = line.split(' ')[1::2]
        cnt = int(cnt)
        von = int(von) - 1
        zu = int(zu) - 1
        x = crates[von][:cnt]
        crates[von] = crates[von][cnt:]

        x.reverse()
        crates[zu] = x + crates[zu]
    returnstring = ''
    for i in crates:
        returnstring += i[0]
    print(returnstring)


def main():
    read_data()

    # global data

    solution()


if __name__ == '__main__':
    main()
