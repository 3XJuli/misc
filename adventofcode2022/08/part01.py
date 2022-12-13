import math
import pprint

data = []
INPUT_PATH: str = 'input'

seen_trees: dict = {}


def read_data():
    global data
    with open(INPUT_PATH, 'r') as f:
        for line in f.readlines():
            data += [line.strip()]


read_data()

# data = ['30373', '25512', '65332', '33549', '35390']


def solution():
    left()
    right()
    bottom()
    top()
    pprint.pprint(seen_trees)
    print(len(seen_trees))



def left():
    global seen_trees
    for row, line in enumerate(data):
        see_height = int(line[0])
        seen_trees[row, 0] = 1
        max_height = see_height
        for col, tree in enumerate(line[1:], start=1):
            tree_height = int(tree)
            if tree_height > max_height:
                seen_trees[row, col] = 1
                max_height = tree_height


def right():
    global seen_trees
    for row, line in enumerate(data):
        seen_trees[row, len(line) - 1] = 1
        max_height = int(line[-1])
        for col, tree in enumerate(line[-2::-1], start=1):
            tree_height = int(tree)
            col = len(line) - 1 - col
            print(row, col)
            if tree_height > max_height:
                seen_trees[row, col] = 1
                max_height = tree_height


def top():
    global seen_trees
    curr_line = curr_max_heights = data[0]
    curr_max_heights = list(curr_max_heights)
    for col, tree in enumerate(curr_line):
        seen_trees[0, col] = 1

    for row, line in enumerate(data[1:], start=1):
        for col, tree in enumerate(line):
            tree_height = int(tree)
            if tree_height > int(curr_max_heights[col]):
                seen_trees[row, col] = 1
                curr_max_heights[col] = tree_height


def bottom():
    global seen_trees
    curr_line = curr_max_heights = data[-1]
    curr_max_heights = [int(i) for i in list(curr_max_heights)]
    init_row = len(data) - 1  # last row
    for col, tree in enumerate(curr_line):
        seen_trees[init_row, col] = 1

    for row, line in enumerate(data[-2::-1], start=1):
        row = len(data) - 1 - row
        for col, tree in enumerate(line):
            tree_height = int(tree)
            if tree_height > curr_max_heights[col]:
                seen_trees[row,  col] = 1
                curr_max_heights[col] = tree_height


def main():
    solution()


if __name__ == '__main__':
    main()
