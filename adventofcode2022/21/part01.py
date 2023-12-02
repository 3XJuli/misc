import math
from typing import Optional, Union

data: list[str] = []
INPUT_PATH: str = 'input'
# INPUT_PATH: str = 'sample1'

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
            value = int(operation)
            monkey = Monkey(monkey_name, value, determined)
            monkeys[monkey_name] = monkey


        else:
            child_a = operation[:4]
            child_b = operation[7:]
            operation = operation[5]

            monkey = Monkey(monkey_name, -1, False, child_a, child_b, operation)
            if monkey_name == 'root':
                root = monkey

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


def dfs(curr_monkey: Monkey = root) -> int:
    global monkeys
    if curr_monkey.determined:
        return curr_monkey.value
    else:

        left_child = monkeys[curr_monkey.child_a]
        right_child = monkeys[curr_monkey.child_b]

        left_value = dfs(left_child)
        right_value= dfs(right_child)

        curr_monkey.determined = True
        new_value = calculate(left_value, right_value, curr_monkey.operation)

        return int(new_value)


def solution():
    return 0


def main():
    # global data

    create_monkeys()
    print(dfs(root))


if __name__ == '__main__':
    main()
