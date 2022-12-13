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

def scenic_score(tree, row, col):

    mtree = tree
    lscore = 0
    rscore = 0
    tscore = 0
    bscore = 0

    if row == 2 and col == 0:
        print("aa")

    # lscore
    if col-1 >= 0:
        for tree in data[row][col-1::-1]:
            lscore += 1
            if int(tree) >= mtree:
                break

    # rscore
    for tree in data[row][col+1::]:
        rscore += 1
        if int(tree) >= mtree:
            break

    #tscore
    for line in data[row+1::]:
        tree = line[col]
        tscore += 1
        if int(tree) >= mtree:
            break

    #bscore
    if row-1 >= 0:
        for line in data[row-1::-1]:
            tree = line[col]
            bscore += 1
            if int(tree) >= mtree:
                break
    return lscore * rscore * tscore * bscore



def solution():
    highest_score = 0
    for row, line in enumerate(data):
        for col, tree in enumerate(line):
            score = scenic_score(int(tree), row, col)
            if score > highest_score:
                print(row, col)
                highest_score = score

    print(highest_score)





def main():
    solution()


if __name__ == '__main__':
    main()
