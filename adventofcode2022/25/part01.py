import math
data = []
INPUT_PATH: str = 'input'
# INPUT_PATH: str = 'sample'


with open(INPUT_PATH, 'r') as f:
    for line in f.readlines():
        data += [line.strip('\n')]


def balanced_pow5_to_dec(l: str):
    number = 0
    power = 0
    for ch in reversed(l):
        match ch:
            case '-': number -= pow(5, power)
            case '=': number -= 2*pow(5, power)
            case _: number += int(ch) * pow(5, power)
        power += 1
    return number


lookup_pow5 = [pow(5, i) for i in range(41)]



def dec_to_pow5(number: int) -> list[...]:
    global lookup_pow5

    if not number:
        return [0]

    pow5_number = list()
    start_potency = 0
    for ix, power in enumerate(lookup_pow5):
        if not number // power:
            start_potency = ix - 1
            break

    remainder = number
    potency = start_potency
    while potency >= 0:
        highest_power = lookup_pow5[potency]
        new_digit = remainder // highest_power
        pow5_number.append(new_digit)
        if new_digit:
            remainder = remainder % (new_digit * highest_power)
        potency -= 1

    return pow5_number

def pow5_to_balanced_pow5(number: list[...]) -> list[...]:
    balanced_pow5: list[...] = number[::-1]
    ix = 0
    while ix < len(balanced_pow5):
        if 3 <= balanced_pow5[ix]:
            if ix == len(balanced_pow5) - 1:
                balanced_pow5.append(0)
            # potencies over 5, e.g. if we pushed back until 10 or something which could probably happen
            multiplicity = (balanced_pow5[ix] // 5) * lookup_pow5[ix]
            balanced_pow5[ix] -= multiplicity
            balanced_pow5[ix] += multiplicity

            # now, we are between 3 and 4, therefore we introduce minus (-2, -1) in this spot and push back one potency
            balanced_pow5[ix] -= 5
            balanced_pow5[ix + 1] += 1
        ix += 1




    return balanced_pow5[::-1]



def _cout(number: list[...]):
    print(''.join([str(num) if num >= 0 else '=' if num == -2 else '-' for num in number ]))


def solution():
    total = 0
    for line in data:
        total += balanced_pow5_to_dec(line)


    result = pow5_to_balanced_pow5(dec_to_pow5(total))
    _cout(result)



def main():
    # global data

    solution()


if __name__ == '__main__':
    main()
