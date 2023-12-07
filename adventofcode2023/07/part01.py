import math
from collections import defaultdict

data = []
INPUT_PATH: str = "input"
# INPUT_PATH: str = "debug_input"


with open(INPUT_PATH, "r") as f:
    for line in f.readlines():
        data += [line.strip("\n").split()]


class Cards:
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = int(bid)

    def __repr__(self) -> str:
        return str(self.__dict__)

    def get_rank(self) -> int:
        cnt: defaultdict[str, int] = defaultdict(int)
        for crd in self.cards:
            cnt[crd] += 1

        cnts = sorted(list(cnt.values()))

        if cnts == [5]:
            return 1
        elif cnts == [1, 4]:
            return 2
        elif cnts == [2, 3]:
            return 3
        elif cnts == [1, 1, 3]:
            return 4
        elif cnts == [1, 2, 2]:
            return 5
        elif cnts == [1, 1, 1, 2]:
            return 6
        elif cnts == [1, 1, 1, 1, 1]:
            return 7

        raise ValueError()

    def _get_val(self, ch: str) -> int:
        if ch.isdigit():
            return int(ch)
        else:
            match ch:
                case "A":
                    return 14
                case "K":
                    return 13
                case "Q":
                    return 12
                case "J":
                    return 11
                case "T":
                    return 10
                case _:
                    raise ValueError()

    def _compare_cards(self, other: "Cards"):
        for i, card in enumerate(self.cards):
            val_self = self._get_val(card)
            val_other = self._get_val(other.cards[i])
            if val_self < val_other:
                return True
            elif val_other < val_self:
                return False

    def __lt__(self, other: "Cards"):
        own_rank = self.get_rank()
        other_rank = other.get_rank()

        if own_rank < other_rank:
            return False
        if other_rank < own_rank:
            return True
        if other_rank == own_rank:
            return self._compare_cards(other)

    def __gt__(self, other: "Cards"):
        return not (self < other)


card_data = [Cards(dt[0], dt[1]) for dt in data]


def solution():
    out = 0
    sorted_cards = sorted(card_data)

    for i, card in enumerate(sorted_cards):
        out += (i + 1) * card.bid

    print(out)


def main():
    # global data

    solution()


if __name__ == "__main__":
    main()
