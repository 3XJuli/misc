import math

data: list[str] = []
INPUT_PATH: str = 'input'
# INPUT_PATH: str = 'sample1'


def read_data():
    global data
    with open(INPUT_PATH, 'r') as f:
        for line in f.readlines():
            data += [line.strip('\n')]


n = 0
monkey_items = []

# mult = true
# plus = false
# op = 0
# num = 1
operations = []
divisible = []

# true, false
cases = []

inspected_items: list = []

items_past: list = []


def parse():
    global n
    ix = 0
    for line in data:
        match ix % 7:
            case 0:
                n += 1
            case 1:
                monkey_items.append(eval('[' + line[18:] + ']'))
            case 2:
                operations.append((line[23:24] == '*', int(line[25:]) if line[25:] != "old" else -1))
            case 3:
                divisible.append(int(line[21:]))
            case 4:
                cases.append([int(line[-1]), -1])
            case 5:
                cases[-1][1] = int(line[-1])
            case 6:
                ix = -1
        ix += 1

    global inspected_items
    inspected_items = [0] * n


def solution():
    parse()
    rounds = 10_000

    global inspected_items
    global cases
    global divisible
    global operations
    global monkey_items
    global n
    global items_past

    items_past = []

    # print(monkey_items)
    # print(cases)
    y = 2 * 7 * 13 * 3 * 19 * 5 * 17 * 11
    for r in range(rounds):
        # if r % 5 == 0:
        for m in range(n):
            print(monkey_items)
            while monkey_items[m]:
                inspected_items[m] += 1
                old_item = monkey_items[m].pop(0)
                operation_y = operations[m][1]if operations[m][1] >= 0 else old_item
                new_item = (old_item * operation_y if operations[m][0] else old_item + operation_y)
                new_item = new_item % y

                item_mod = (new_item % divisible[m]) == 0

                new_monkey = cases[m][0] if item_mod else cases[m][1]

                monkey_items[new_monkey].append(new_item)

    sorted_items = sorted(inspected_items)
    output = sorted_items[-1] * sorted_items[-2]

    # print(sorted_items)
    print(output)
    # print(inspected_items)


def main():
    read_data()

    # global data

    solution()


if __name__ == '__main__':
    main()
