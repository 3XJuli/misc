import math

data = []
INPUT_PATH: str = "input"
#  INPUT_PATH: str = "debug_input"


with open(INPUT_PATH, "r") as f:
    for line in f.readlines():
        data += [line.strip("\n")]


def solution():
    out = 0

    original_cards = []
    for i, line in enumerate(data):
        card_data = line.split(": ")[1]
        winning_numbers_raw, my_numbers_raw = card_data.split(" | ")
        winning_numbers = winning_numbers_raw.split()
        my_numbers = my_numbers_raw.split()

        original_cards.append((winning_numbers, my_numbers))

    card_counts = [1] * len(original_cards)

    for i, card_count in enumerate(card_counts):
        winning_numbers, my_numbers = original_cards[i]
        added_card_index = i + 1
        out += card_count
        for number in my_numbers:
            if number in winning_numbers:
                card_counts[added_card_index] += card_count
                added_card_index += 1

    print(out)


def main():
    # global data

    solution()


if __name__ == "__main__":
    main()
