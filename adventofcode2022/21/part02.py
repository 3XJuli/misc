import math
from typing import Optional, Union

data: list[str] = []
INPUT_PATH: str = 'input'
# INPUT_PATH: str = 'sample'

with open(INPUT_PATH, 'r') as f:
    for line in f.readlines():
        data += [line.strip('\n')]


class Monkey(object):
    def __init__(self, name, value: Union[int, str], determined: bool, child_a: str = '', child_b: str = '',
                 operation: chr = ''):
        self.name = name
        self.value = value
        self.child_a: str = child_a
        self.child_b: str = child_b
        self.operation: chr = operation
        self.determined = determined
        self.contains_humn = False

    def __repr__(self):
        return str(self.__dict__)


monkeys: dict[str, Monkey] = {}
root: Optional[Monkey] = None


def create_monkeys():
    global root
    for l in data:
        monkey_name, operation = l.split(': ')
        if len(operation) <= 4:
            determined = True
            ca = ''
            cb = ''
            value = int(operation)
            monkey = Monkey(monkey_name, value, determined)
            if monkey_name == 'humn':
                monkey.value = 'x'
                monkey.contains_humn = True
            monkeys[monkey_name] = monkey


        else:
            child_a = operation[:4]
            child_b = operation[7:]
            operation = operation[5]

            monkey = Monkey(monkey_name, -1, False, child_a, child_b, operation)
            if monkey_name == 'root':
                monkey.operation = '='
                root = monkey
            # print(monkey_name)

            monkeys[monkey_name] = monkey


def calculate(l_v, r_v, op) -> float:
    assert isinstance(l_v, float) or isinstance(l_v, int)
    assert isinstance(r_v, int) or isinstance(r_v, float)
    match op:
        case '*':
            return l_v * r_v
        case '/':
            return l_v / r_v
        case '+':
            return l_v + r_v
        case '-':
            return l_v - r_v
        case '=':
            return l_v == r_v


def inverse(left: list, right: int, op: str):
    match op:
        case '*':
            return [left, '/', right]
        case '/':
            return [left, '*', right]
        case '+':
            return [left, '-', right]
        case '-':
            return [left, '+', right]
        case _:
            assert False


def l_inverse(left: list, right: int, op: str):
    match op:
        case '*':
            return ['/', right, left]
        case '/':
            return ['*', right, left]
        case '+':
            return ['-', right, left]
        case '-':
            return ['+', right, left]
        case _:
            assert False


def r_inverse(left: int, right: list, op: str):
    match op:
        case '*':
            return ['/', left, right]
        case '/':
            return [right, left, '/']
        case '+':
            return ['-', left, right]
        case '-':
            return [right, left, '-']
        case _:
            assert False


def dfs(curr_monkey: Monkey = root) -> tuple[Union[list, int], bool]:
    global monkeys
    if curr_monkey.determined:
        return [curr_monkey.value], curr_monkey.contains_humn
    else:

        left_child = monkeys[curr_monkey.child_a]
        right_child = monkeys[curr_monkey.child_b]

        left_value, l_contains_humn = dfs(left_child)
        right_value, r_contains_humn = dfs(right_child)

        if curr_monkey.name == 'root':
            if l_contains_humn:
                inverse_operations = left_value
                y = right_value[0]
            else:
                inverse_operations = right_value[0]
                y = left_value[0]

            while len(inverse_operations) == 3:
                if isinstance(inverse_operations[0], str):
                    op = inverse_operations[0]
                    y = calculate(y, inverse_operations[1], op)
                    inverse_operations = inverse_operations[2]
                else:
                    op = inverse_operations[2]
                    y = calculate(inverse_operations[1], y, op)
                    inverse_operations = inverse_operations[0]
            return int(y), True

        if l_contains_humn or r_contains_humn:
            curr_monkey.contains_hmn = True

        if right_child.contains_humn and left_child.contains_humn:
            assert False

        if l_contains_humn:
            curr_monkey.determined = True
            new_value = l_inverse(left_value, right_value[0], curr_monkey.operation)
            return new_value, True
        elif r_contains_humn:
            curr_monkey.determined = True
            new_value = r_inverse(left_value[0], right_value, curr_monkey.operation)
            return new_value, True
        else:
            curr_monkey.determined = True
            new_value = calculate(left_value[0], right_value[0], curr_monkey.operation)
            curr_monkey.determined = True
            return [new_value], False


def solution():
    return 0


def main():
    # global data

    create_monkeys()
    print(dfs(root)[0])


if __name__ == '__main__':
    main()
